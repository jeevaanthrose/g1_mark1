# G1 Mark 1 — 12-DOF Humanoid Robot

A custom development project focused on the simulation and keyboard-based teleoperation of a **12-DOF Unitree G1 humanoid robot** using **MuJoCo**.

This repository contains the custom development work for **G1 Mark 1**, including the 12-DOF robot model, MuJoCo configuration, and WASD-based teleoperation.

---

## 🚀 Project Overview

**G1 Mark 1** is a custom humanoid robotics development project focused on building and experimenting with a **12-DOF Unitree G1 humanoid robot** in simulation.

The current implementation focuses on:

* 12-DOF humanoid robot simulation
* MuJoCo-based simulation
* WASD keyboard teleoperation
* Custom G1 12-DOF robot description
* URDF and MuJoCo XML models
* Custom deployment configuration
* Foundation for future LiDAR integration
* Foundation for SLAM and autonomous navigation development

The project is currently under active development.

---

## ✨ Current Features

* ✅ G1 12-DOF robot model
* ✅ MuJoCo simulation
* ✅ WASD keyboard teleoperation
* ✅ Forward and backward movement
* ✅ Left and right movement
* ✅ Custom G1 configuration
* ✅ Custom URDF robot description
* ✅ Custom MuJoCo XML model
* 🔄 LiDAR integration and development
* 🔄 SLAM implementation and improvements
* 🔄 Autonomous navigation
* 🔄 ROS 2 integration

---

## 📁 Repository Structure

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
└── README.md
```

### Key Files

| File                              | Description                                                       |
| --------------------------------- | ----------------------------------------------------------------- |
| `g1_12dof_wasd.py`                | Main 12-DOF G1 MuJoCo simulation and WASD teleoperation script    |
| `g1_12dof_wasd_WORKING_BACKUP.py` | Backup of the working G1 12-DOF WASD teleoperation implementation |
| `g1.yaml`                         | G1 deployment and simulation configuration                        |
| `g1_12dof.xml`                    | MuJoCo XML model description of the G1 12-DOF robot               |
| `g1_12dof.urdf`                   | URDF description of the G1 12-DOF robot                           |

---

## 🛠️ Requirements

The project requires:

* Ubuntu Linux
* Python 3
* Python virtual environment
* MuJoCo
* NumPy
* PyTorch
* PyYAML
* Unitree `legged_gym` framework

The project was developed and tested using a Python virtual environment named:

```text
g1_rl_env
```

The custom G1 Mark 1 code is maintained separately from the underlying Unitree framework.

---

## 🔗 Base Framework

G1 Mark 1 uses the **Unitree RL Gym framework** as the underlying robotics and reinforcement-learning environment.

The official framework is available here:

**Official Unitree RL Gym Repository**

https://github.com/unitreerobotics/unitree_rl_gym

This repository contains the **custom G1 Mark 1 development work** built using the underlying framework.

The official Unitree repository is not included in this repository. Users should obtain the required framework separately.

---

# ⚙️ Setup

## 1. Clone the Official Unitree RL Gym Framework

Clone the official framework:

```bash
git clone https://github.com/unitreerobotics/unitree_rl_gym.git
```

The default location used in this project is:

```text
~/unitree_rl_gym
```

The `legged_gym` package required by the G1 Mark 1 deployment script is provided by this framework.

---

## 2. Clone the G1 Mark 1 Repository

Clone this repository:

```bash
git clone https://github.com/jeevaanthrose/g1_mark1.git
```

The default project location used in this documentation is:

```text
~/g1_mark1
```

---

## 3. Activate the Python Environment

Activate the environment used for the project:

```bash
source ~/g1_rl_env/bin/activate
```

Verify that the environment is active:

```bash
which python
```

The terminal should show the Python interpreter associated with the `g1_rl_env` environment.

---

# 🚀 Running G1 Mark 1

Navigate to the G1 Mark 1 project:

```bash
cd ~/g1_mark1
```

Activate the Python environment:

```bash
source ~/g1_rl_env/bin/activate
```

Run the G1 12-DOF MuJoCo simulation with WASD teleoperation:

```bash
PYTHONPATH=$HOME/unitree_rl_gym:$PWD python deploy/deploy_mujoco/g1_12dof_wasd.py g1.yaml
```

The command uses:

```text
~/g1_mark1
        │
        └── Your custom G1 Mark 1 code

~/unitree_rl_gym
        │
        └── Unitree framework and legged_gym dependency
```

The `PYTHONPATH` configuration allows the custom G1 Mark 1 project to access the required `legged_gym` package from the official Unitree RL Gym framework.

---

## 🖥️ Expected Result

After successfully launching the script, the **MuJoCo simulation window** should open with the **G1 12-DOF humanoid robot** loaded.

The robot can then be controlled using the WASD keyboard teleoperation interface.

A successful run should result in:

```text
G1 12-DOF Humanoid Robot
        │
        ▼
MuJoCo Simulation
        │
        ▼
WASD Keyboard Teleoperation
```

> **Note:** The exact terminal output may vary depending on the current implementation and configuration. The main indication of successful execution is that the MuJoCo simulation window launches and the G1 humanoid robot is displayed.

---

# 🎮 WASD Teleoperation

Once the MuJoCo simulation is running, use the keyboard to control the robot.

| Key | Action        |
| --- | ------------- |
| `W` | Move Forward  |
| `S` | Move Backward |
| `A` | Move Left     |
| `D` | Move Right    |

The robot responds to keyboard commands through the custom G1 Mark 1 WASD teleoperation implementation.

---

# 🧠 System Architecture

The current G1 Mark 1 system is structured as follows:

```text
                 G1 MARK 1
                     │
                     ▼
          Custom 12-DOF G1 Model
                     │
                     ▼
             MuJoCo Simulation
                     │
                     ▼
          Custom WASD Teleoperation
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
          W          A          D
       Forward      Left      Right
          │
          ▼
          S
       Backward
```

The project is designed as a foundation for integrating additional perception and autonomy capabilities.

---

# 🤖 Robot Description

The G1 Mark 1 repository contains custom 12-DOF robot descriptions in two formats.

### MuJoCo Model

```text
src/g1_description/g1_12dof.xml
```

Used for:

* MuJoCo simulation
* Robot dynamics
* Joint configuration
* Simulation environment

### URDF Model

```text
src/g1_description/g1_12dof.urdf
```

Used as the robot description for future robotics and ROS-based integration.

---

# 🔬 Development Roadmap

The project is under active development.

## Completed

* [x] G1 12-DOF robot model
* [x] MuJoCo simulation
* [x] WASD keyboard teleoperation
* [x] Custom G1 deployment configuration
* [x] Custom URDF robot description
* [x] Custom MuJoCo XML model
* [x] Clean standalone G1 Mark 1 repository

## In Development

* [ ] LiDAR integration
* [ ] SLAM implementation
* [ ] SLAM map improvements
* [ ] Autonomous navigation
* [ ] ROS 2 integration
* [ ] Path planning
* [ ] Obstacle avoidance
* [ ] Navigation stack integration
* [ ] Extended humanoid autonomy

---

# 📌 Project Status

**Project:** G1 Mark 1

**Current Milestone:**

> **Working 12-DOF G1 Humanoid Robot with WASD Teleoperation in MuJoCo**

**Status:** Active Development

The current focus is on improving the robot simulation, sensor integration, SLAM capabilities, and autonomous navigation pipeline.

---

# 🧪 Development Environment

The project was developed and tested using:

```text
Operating System : Ubuntu Linux
Python Environment: g1_rl_env
Robot            : Unitree G1
Degrees of Freedom: 12-DOF
Simulator        : MuJoCo
Control          : WASD Keyboard Teleoperation
Framework        : Unitree RL Gym / legged_gym
```

---

# 🔗 Project Dependencies

G1 Mark 1 is designed to work with the following external framework:

### Unitree RL Gym

Official repository:

https://github.com/unitreerobotics/unitree_rl_gym

The Unitree RL Gym repository provides the underlying `legged_gym` framework used by the G1 Mark 1 deployment script.

Please refer to the official repository for the framework installation requirements and documentation.

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

Special acknowledgement to the **Unitree RL Gym** project, which provides the underlying framework used in the development of G1 Mark 1.

Official repository:

https://github.com/unitreerobotics/unitree_rl_gym

The original framework, source code, licenses, and attributions belong to their respective authors and contributors.

---

# 📄 License

This repository contains custom development work for the G1 Mark 1 project and relies on external open-source frameworks.

The underlying Unitree RL Gym framework is maintained separately by its original authors.

Please refer to the official Unitree RL Gym repository and its applicable license for the licensing terms of the underlying framework:

https://github.com/unitreerobotics/unitree_rl_gym

Users are responsible for complying with the licenses and terms of any external dependencies used with this project.

---

# ⭐ Future Vision

The long-term goal of G1 Mark 1 is to develop a more capable humanoid robotics platform combining:

```text
Humanoid Robot
      │
      ▼
Sensor Integration
      │
      ├── LiDAR
      ├── IMU
      └── Other Sensors
      │
      ▼
SLAM
      │
      ▼
Environment Mapping
      │
      ▼
Autonomous Navigation
      │
      ▼
Path Planning
      │
      ▼
Humanoid Autonomous System
```

The project will continue evolving toward advanced perception, mapping, navigation, and autonomous humanoid robotics.
