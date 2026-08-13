# G1 Mark 1 — 12-DOF Humanoid Robot

A custom development project focused on the simulation, ROS 2 integration, LiDAR, odometry, and keyboard-based teleoperation of a **12-DOF Unitree G1 humanoid robot** using **MuJoCo**.

G1 Mark 1 is being developed as a foundation for **SLAM, mapping, autonomous navigation, path planning, and humanoid autonomy**.

---

## 🚀 Project Overview

**G1 Mark 1** is a custom humanoid robotics development project built around a **12-DOF Unitree G1 humanoid robot** in simulation.

The current system combines:

* 12-DOF humanoid robot simulation
* MuJoCo-based simulation
* WASD keyboard teleoperation
* Custom G1 12-DOF robot description
* URDF and MuJoCo XML models
* ROS 2 Jazzy integration
* LiDAR simulation
* `/scan` LaserScan publishing
* `/odom` odometry publishing
* TF broadcasting
* Foundation for SLAM and autonomous navigation

The project is under active development.

---

# ✨ Current Features

* ✅ G1 12-DOF robot model
* ✅ MuJoCo simulation
* ✅ WASD keyboard teleoperation
* ✅ Forward and backward movement
* ✅ Left and right movement
* ✅ Custom G1 configuration
* ✅ Custom URDF robot description
* ✅ Custom MuJoCo XML model
* ✅ ROS 2 Jazzy integration
* ✅ Simulated LiDAR
* ✅ `/scan` ROS 2 topic
* ✅ `/odom` ROS 2 topic
* ✅ Dynamic odometry TF
* 🔄 SLAM implementation
* 🔄 SLAM map improvements
* 🔄 Autonomous navigation
* 🔄 Path planning
* 🔄 Obstacle avoidance

---

# 📁 Repository Structure

```text
g1_mark1/
│
├── deploy/
│   └── deploy_mujoco/
│       ├── configs/
│       │   └── g1.yaml
│       │
│       ├── g1_12dof_wasd.py
│       └── g1_12dof_wasd_WORKING_BACKUP.py
│
├── src/
│   └── g1_description/
│       ├── g1_12dof.urdf
│       └── g1_12dof.xml
│
├── g1_mark1
└── README.md
```

### Key Files

| File                              | Description                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| `g1_mark1`                        | One-command G1 Mark 1 launcher                                                       |
| `g1_12dof_wasd.py`                | Main G1 MuJoCo simulation, WASD teleoperation, LiDAR, odometry and ROS 2 integration |
| `g1_12dof_wasd_WORKING_BACKUP.py` | Backup of the working G1 WASD implementation                                         |
| `g1.yaml`                         | G1 deployment and simulation configuration                                           |
| `g1_12dof.xml`                    | MuJoCo model description                                                             |
| `g1_12dof.urdf`                   | URDF robot description                                                               |

---

# 🛠️ Requirements

The project requires:

* Ubuntu Linux
* Python 3
* Python virtual environment
* ROS 2 Jazzy
* MuJoCo
* NumPy
* PyTorch
* PyYAML
* Unitree `legged_gym` framework

The project uses the Python environment:

```text
g1_rl_env
```

The underlying Unitree framework is maintained separately from this repository.

---

# 🔗 Base Framework

G1 Mark 1 uses the **Unitree RL Gym** framework as the underlying robotics and reinforcement-learning environment.

Official repository:

https://github.com/unitreerobotics/unitree_rl_gym

The Unitree RL Gym framework provides the `legged_gym` dependency required by the G1 Mark 1 deployment.

---

# ⚙️ Setup

## 1. Clone Unitree RL Gym

```bash
cd ~
git clone https://github.com/unitreerobotics/unitree_rl_gym.git
```

The expected location is:

```text
~/unitree_rl_gym
```

---

## 2. Clone G1 Mark 1

```bash
cd ~
git clone https://github.com/jeevaanthrose/g1_mark1.git
```

The expected project location is:

```text
~/g1_mark1
```

---

## 3. Python Environment

Create or use the project environment:

```text
g1_rl_env
```

Activate it:

```bash
source ~/g1_rl_env/bin/activate
```

Verify:

```bash
which python
```

---

## 4. ROS 2 Jazzy

The launcher automatically loads:

```bash
source /opt/ros/jazzy/setup.bash
```

ROS 2 Jazzy must therefore be installed on the system.

---

# 🚀 One-Command Launch

The main feature of the current G1 Mark 1 setup is the **one-command launcher**.

After the initial setup, simply run:

```bash
g1_mark1
```

The launcher automatically:

1. Enters `~/g1_mark1`
2. Activates `g1_rl_env`
3. Loads ROS 2 Jazzy
4. Configures `PYTHONPATH`
5. Configures GLFW for X11
6. Starts the G1 12-DOF MuJoCo simulation

The complete workflow becomes:

```text
g1_mark1
    │
    ▼
~/g1_mark1
    │
    ▼
g1_rl_env
    │
    ▼
ROS 2 Jazzy
    │
    ▼
PYTHONPATH
    │
    ▼
GLFW / X11
    │
    ▼
G1 12-DOF MuJoCo
```

No manual `cd`, environment activation, ROS setup, or Python command is required after the launcher is configured.

---

# 🔧 Launcher Configuration

The `g1_mark1` launcher performs the following setup:

```bash
cd "$HOME/g1_mark1"

source "$HOME/g1_rl_env/bin/activate"

source /opt/ros/jazzy/setup.bash

export PYTHONPATH="$HOME/unitree_rl_gym:$HOME/g1_mark1:$PYTHONPATH"

export GLFW_PLATFORM=x11

python deploy/deploy_mujoco/g1_12dof_wasd.py g1.yaml
```

The launcher is intended to provide a consistent startup environment for G1 Mark 1.

---

# 🐛 GLFW / X11

The current simulation uses:

```bash
export GLFW_PLATFORM=x11
```

This is included in the launcher to provide the required GLFW/X11 configuration for the current development environment.

If the graphical environment changes, this configuration may need to be adjusted.

---

# 🖥️ Expected Result

After running:

```bash
g1_mark1
```

the MuJoCo simulation window should open with the **G1 12-DOF humanoid robot**.

The system provides keyboard-based teleoperation together with simulated sensor and ROS 2 data.

Expected architecture:

```text
G1 12-DOF
    │
    ▼
MuJoCo Simulation
    │
    ├──────────────► WASD Teleoperation
    │
    ├──────────────► LiDAR
    │                    │
    │                    ▼
    │                  /scan
    │
    └──────────────► Odometry
                         │
                         ▼
                       /odom
```

---

# 🎮 WASD Teleoperation

Once the simulation is running:

| Key | Action        |
| --- | ------------- |
| `W` | Move Forward  |
| `S` | Move Backward |
| `A` | Move Left     |
| `D` | Move Right    |

The commands are handled by the custom G1 Mark 1 teleoperation implementation.

---

# 🤖 ROS 2 Integration

G1 Mark 1 currently includes ROS 2 integration for simulated sensor and robot-state data.

## ROS 2 Topics

### LiDAR

```text
/scan
```

Message type:

```text
sensor_msgs/msg/LaserScan
```

The simulated LiDAR publishes LaserScan data for future perception and SLAM development.

### Odometry

```text
/odom
```

Message type:

```text
nav_msgs/msg/Odometry
```

The simulation publishes odometry information representing the robot's simulated motion.

---

# 🔄 TF

The current implementation provides TF broadcasting for the robot.

The system includes:

```text
odom
  │
  ▼
pelvis
  │
  ▼
lidar_link
```

The odometry transform is dynamically updated during simulation.

The LiDAR transform is provided as a static transform.

This TF structure is intended to support future ROS 2 SLAM and navigation integration.

---

# 📡 LiDAR

G1 Mark 1 includes a simulated LiDAR system inside the MuJoCo environment.

The LiDAR data is published through:

```text
/scan
```

with:

```text
sensor_msgs/msg/LaserScan
```

The LiDAR subsystem is currently being developed as the perception foundation for:

* SLAM
* Mapping
* Obstacle detection
* Navigation
* Path planning

---

# 🧭 Odometry

The simulation publishes robot odometry through:

```text
/odom
```

using:

```text
nav_msgs/msg/Odometry
```

The odometry system is used as a foundation for integrating:

* SLAM
* Localization
* Navigation
* Path planning

---

# 🧠 System Architecture

The current G1 Mark 1 architecture is:

```text
                  G1 MARK 1
                      │
                      ▼
             Custom 12-DOF G1
                      │
                      ▼
              MuJoCo Simulation
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
        WASD        LiDAR       Odometry
          │           │           │
          ▼           ▼           ▼
       Motion       /scan       /odom
                      │
                      ▼
                    SLAM
                      │
                      ▼
                  Mapping
                      │
                      ▼
             Autonomous Navigation
```

---

# 🤖 Robot Description

G1 Mark 1 contains custom 12-DOF robot descriptions.

## MuJoCo Model

```text
src/g1_description/g1_12dof.xml
```

Used for:

* MuJoCo simulation
* Robot dynamics
* Joint configuration
* Sensor configuration
* Simulation environment

## URDF Model

```text
src/g1_description/g1_12dof.urdf
```

Used as the robot description for ROS-based robotics development and future integration.

---

# 🔬 Development Roadmap

## Completed

* ✅ G1 12-DOF robot model
* ✅ MuJoCo simulation
* ✅ WASD keyboard teleoperation
* ✅ Forward/backward movement
* ✅ Left/right movement
* ✅ Custom G1 deployment configuration
* ✅ Custom URDF robot description
* ✅ Custom MuJoCo XML model
* ✅ Standalone G1 Mark 1 repository
* ✅ ROS 2 Jazzy integration
* ✅ Simulated LiDAR
* ✅ `/scan` LaserScan publishing
* ✅ `/odom` Odometry publishing
* ✅ Dynamic odometry TF
* ✅ One-command G1 simulation launcher

## In Development

* 🔄 SLAM implementation
* 🔄 SLAM map improvements
* 🔄 Localization
* 🔄 Autonomous navigation
* 🔄 Path planning
* 🔄 Obstacle avoidance
* 🔄 Navigation stack integration
* 🔄 Extended humanoid autonomy

---

# 📌 Project Status

**Project:** G1 Mark 1

**Robot:** Unitree G1

**Degrees of Freedom:** 12-DOF

**Current Milestone:**

> **Working 12-DOF G1 Humanoid Robot with MuJoCo Simulation, WASD Teleoperation, LiDAR, Odometry, and ROS 2 Integration**

**Status:** Active Development

The current development focus is on improving:

* LiDAR perception
* Odometry
* SLAM
* Mapping
* Localization
* Autonomous navigation

---

# 🧪 Development Environment

```text
Operating System : Ubuntu Linux
ROS Version      : ROS 2 Jazzy
Python Environment: g1_rl_env
Robot            : Unitree G1
Degrees of Freedom: 12-DOF
Simulator        : MuJoCo
Control          : WASD Keyboard Teleoperation
Framework        : Unitree RL Gym / legged_gym
ROS Topics       : /scan, /odom
```

---

# 🔗 Project Dependencies

## Unitree RL Gym

Official repository:

https://github.com/unitreerobotics/unitree_rl_gym

The Unitree RL Gym framework provides the underlying `legged_gym` environment used by G1 Mark 1.

The official framework is maintained separately from this repository.

Users should refer to the official repository for framework installation requirements and documentation.

---

# 👨‍💻 Author

## Jeeva Anthrose S

**Robotics & Automation Engineer**

Areas of interest:

* Robotics
* Humanoid Robots
* Autonomous Systems
* ROS 2
* SLAM
* Computer Vision
* Artificial Intelligence
* Machine Learning
* Embedded Systems
* Robot Simulation

---

# 🙏 Acknowledgements

This project builds upon the work of **Unitree Robotics** and the open-source robotics community.

Special acknowledgement to the **Unitree RL Gym** project, which provides the underlying framework used in G1 Mark 1.

Official repository:

https://github.com/unitreerobotics/unitree_rl_gym

The original framework, source code, licenses, and attributions belong to their respective authors and contributors.

---

# 📄 License

This repository contains custom development work for the G1 Mark 1 project and relies on external open-source frameworks.

The underlying Unitree RL Gym framework is maintained separately by its original authors.

Please refer to the official Unitree RL Gym repository and its applicable license for the licensing terms of the underlying framework.

Users are responsible for complying with the licenses and terms of any external dependencies used with this project.

---

# ⭐ Future Vision

The long-term goal of G1 Mark 1 is to develop a more capable humanoid robotics platform combining simulation, perception, mapping, localization, and autonomous navigation.

```text
                  Humanoid Robot
                        │
                        ▼
                 Sensor Integration
                        │
             ┌──────────┼──────────┐
             │          │          │
           LiDAR       IMU      Other Sensors
             │
             ▼
            SLAM
             │
             ▼
       Environment Mapping
             │
             ▼
          Localization
             │
             ▼
    Autonomous Navigation
             │
             ▼
        Path Planning
             │
             ▼
      Obstacle Avoidance
             │
             ▼
     Humanoid Autonomous System
```

G1 Mark 1 will continue evolving toward advanced perception, mapping, navigation, and autonomous humanoid robotics.
