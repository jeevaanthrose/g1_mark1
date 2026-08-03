import time
import threading
import argparse

import mujoco
import mujoco.viewer
import numpy as np
import torch
import yaml

from legged_gym import LEGGED_GYM_ROOT_DIR


# ============================================================
# Keyboard controller
# ============================================================

class KeyboardController:
    def __init__(self):
        self.cmd = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.running = True
        self.lock = threading.Lock()

        print("\n========================================")
        print("       G1 12-DOF WASD TELEOPERATION")
        print("========================================")
        print(" W : Forward")
        print(" S : Backward")
        print(" A : Turn Left")
        print(" D : Turn Right")
        print(" Q : Forward + Turn Left")
        print(" E : Forward + Turn Right")
        print(" X : Stop")
        print(" ESC : Quit")
        print("========================================\n")

    def set_command(self, key):
        with self.lock:

            # Forward
            if key == "w":
                self.cmd[:] = [0.5, 0.0, 0.0]

            # Backward
            elif key == "s":
                self.cmd[:] = [-0.5, 0.0, 0.0]

            # Turn left
            elif key == "a":
                self.cmd[:] = [0.0, 0.0, 0.5]

            # Turn right
            elif key == "d":
                self.cmd[:] = [0.0, 0.0, -0.5]

            # Forward + left
            elif key == "q":
                self.cmd[:] = [0.5, 0.0, 0.5]

            # Forward + right
            elif key == "e":
                self.cmd[:] = [0.5, 0.0, -0.5]

            # Stop
            elif key == "x":
                self.cmd[:] = [0.0, 0.0, 0.0]

            # Quit
            elif key == "\x1b":
                self.cmd[:] = [0.0, 0.0, 0.0]
                self.running = False

    def get_command(self):
        with self.lock:
            return self.cmd.copy()


# ============================================================
# Non-blocking keyboard input
# ============================================================

def keyboard_thread(controller):

    try:
        import sys
        import tty
        import termios
        import select

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        tty.setcbreak(fd)

        while controller.running:

            if select.select([sys.stdin], [], [], 0.05)[0]:

                key = sys.stdin.read(1).lower()

                controller.set_command(key)

                if key == "\x1b":
                    break

    except Exception as e:
        print("Keyboard input error:", e)

    finally:
        try:
            termios.tcsetattr(
                fd,
                termios.TCSADRAIN,
                old_settings
            )
        except Exception:
            pass


# ============================================================
# Gravity orientation
# ============================================================

def get_gravity_orientation(quaternion):

    qw = quaternion[0]
    qx = quaternion[1]
    qy = quaternion[2]
    qz = quaternion[3]

    gravity_orientation = np.zeros(3)

    gravity_orientation[0] = (
        2 * (-qz * qx + qw * qy)
    )

    gravity_orientation[1] = (
        -2 * (qz * qy + qw * qx)
    )

    gravity_orientation[2] = (
        1 - 2 * (qw * qw + qz * qz)
    )

    return gravity_orientation


# ============================================================
# PD Controller
# ============================================================

def pd_control(
    target_q,
    q,
    kp,
    target_dq,
    dq,
    kd
):

    return (
        (target_q - q) * kp
        + (target_dq - dq) * kd
    )


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "config_file",
        type=str,
        help="Configuration file in deploy/deploy_mujoco/configs"
    )

    args = parser.parse_args()

    config_file = args.config_file

    # --------------------------------------------------------
    # Load configuration
    # --------------------------------------------------------

    config_path = (
        f"{LEGGED_GYM_ROOT_DIR}/deploy/"
        f"deploy_mujoco/configs/{config_file}"
    )

    with open(config_path, "r") as f:

        config = yaml.load(
            f,
            Loader=yaml.FullLoader
        )

    policy_path = config["policy_path"].replace(
        "{LEGGED_GYM_ROOT_DIR}",
        LEGGED_GYM_ROOT_DIR
    )

    xml_path = config["xml_path"].replace(
        "{LEGGED_GYM_ROOT_DIR}",
        LEGGED_GYM_ROOT_DIR
    )

    simulation_duration = config[
        "simulation_duration"
    ]

    simulation_dt = config[
        "simulation_dt"
    ]

    control_decimation = config[
        "control_decimation"
    ]

    kps = np.array(
        config["kps"],
        dtype=np.float32
    )

    kds = np.array(
        config["kds"],
        dtype=np.float32
    )

    default_angles = np.array(
        config["default_angles"],
        dtype=np.float32
    )

    ang_vel_scale = config[
        "ang_vel_scale"
    ]

    dof_pos_scale = config[
        "dof_pos_scale"
    ]

    dof_vel_scale = config[
        "dof_vel_scale"
    ]

    action_scale = config[
        "action_scale"
    ]

    cmd_scale = np.array(
        config["cmd_scale"],
        dtype=np.float32
    )

    num_actions = config[
        "num_actions"
    ]

    num_obs = config[
        "num_obs"
    ]

    # --------------------------------------------------------
    # Initial controller state
    # --------------------------------------------------------

    action = np.zeros(
        num_actions,
        dtype=np.float32
    )

    target_dof_pos = default_angles.copy()

    obs = np.zeros(
        num_obs,
        dtype=np.float32
    )

    counter = 0

    # --------------------------------------------------------
    # Load MuJoCo model
    # --------------------------------------------------------

    print("\nLoading MuJoCo model...")

    m = mujoco.MjModel.from_xml_path(
        xml_path
    )

    d = mujoco.MjData(m)

    m.opt.timestep = simulation_dt

    print("MuJoCo model loaded.")

    # --------------------------------------------------------
    # Load policy
    # --------------------------------------------------------

    print("Loading policy...")

    policy = torch.jit.load(
        policy_path
    )

    policy.eval()

    print("Policy loaded.")

    # --------------------------------------------------------
    # Start keyboard controller
    # --------------------------------------------------------

    controller = KeyboardController()

    keyboard = threading.Thread(
        target=keyboard_thread,
        args=(controller,),
        daemon=True
    )

    keyboard.start()

    # --------------------------------------------------------
    # Start MuJoCo
    # --------------------------------------------------------

    with mujoco.viewer.launch_passive(
        m,
        d
    ) as viewer:

        start = time.time()

        while (
            viewer.is_running()
            and controller.running
            and time.time() - start
            < simulation_duration
        ):

            step_start = time.time()

            # ------------------------------------------------
            # PD control
            # ------------------------------------------------

            tau = pd_control(

                target_dof_pos,

                d.qpos[7:],

                kps,

                np.zeros_like(kds),

                d.qvel[6:],

                kds
            )

            d.ctrl[:] = tau

            # ------------------------------------------------
            # MuJoCo physics step
            # ------------------------------------------------

            mujoco.mj_step(
                m,
                d
            )

            counter += 1

            # ------------------------------------------------
            # Policy update
            # ------------------------------------------------

            if (
                counter
                % control_decimation
                == 0
            ):

                # Current command from keyboard
                cmd = controller.get_command()

                # --------------------------------------------
                # Joint position
                # --------------------------------------------

                qj = d.qpos[7:]

                dqj = d.qvel[6:]

                quat = d.qpos[3:7]

                omega = d.qvel[3:6]

                # --------------------------------------------
                # Normalize observations
                # --------------------------------------------

                qj = (
                    qj - default_angles
                ) * dof_pos_scale

                dqj = (
                    dqj
                    * dof_vel_scale
                )

                gravity_orientation = (
                    get_gravity_orientation(
                        quat
                    )
                )

                omega = (
                    omega
                    * ang_vel_scale
                )

                # --------------------------------------------
                # Gait phase
                # --------------------------------------------

                period = 0.8

                count = (
                    counter
                    * simulation_dt
                )

                phase = (
                    count
                    % period
                ) / period

                sin_phase = np.sin(
                    2
                    * np.pi
                    * phase
                )

                cos_phase = np.cos(
                    2
                    * np.pi
                    * phase
                )

                # --------------------------------------------
                # Create observation
                # --------------------------------------------

                obs[:3] = omega

                obs[3:6] = (
                    gravity_orientation
                )

                obs[6:9] = (
                    cmd
                    * cmd_scale
                )

                obs[
                    9:
                    9 + num_actions
                ] = qj

                obs[
                    9 + num_actions:
                    9 + 2 * num_actions
                ] = dqj

                obs[
                    9 + 2 * num_actions:
                    9 + 3 * num_actions
                ] = action

                obs[
                    9 + 3 * num_actions:
                    9 + 3 * num_actions + 2
                ] = np.array(
                    [
                        sin_phase,
                        cos_phase
                    ]
                )

                # --------------------------------------------
                # Policy inference
                # --------------------------------------------

                obs_tensor = (
                    torch
                    .from_numpy(obs)
                    .unsqueeze(0)
                )

                action = (
                    policy(
                        obs_tensor
                    )
                    .detach()
                    .numpy()
                    .squeeze()
                )

                # --------------------------------------------
                # Target joint positions
                # --------------------------------------------

                target_dof_pos = (
                    action
                    * action_scale
                    + default_angles
                )

            # ------------------------------------------------
            # Update viewer
            # ------------------------------------------------

            viewer.sync()

            # ------------------------------------------------
            # Timing
            # ------------------------------------------------

            time_until_next_step = (
                m.opt.timestep
                - (
                    time.time()
                    - step_start
                )
            )

            if time_until_next_step > 0:

                time.sleep(
                    time_until_next_step
                )

    print("\nG1 12-DOF teleoperation stopped.")
