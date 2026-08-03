# G1 Mark 1 — 12-DOF Humanoid Robot

A custom development project focused on the simulation and keyboard-based teleoperation of a **12-DOF Unitree G1 humanoid robot** using **MuJoCo**.

This repository contains the custom files and development work for **G1 Mark 1**, including a 12-DOF robot model, MuJoCo configuration, and WASD-based teleoperation.

---

## 🚀 Project Overview

**G1 Mark 1** is a custom humanoid robotics development project built around the **Unitree G1 humanoid robot**.

The current implementation focuses on:

* 12-DOF humanoid robot simulation
* MuJoCo-based simulation
* WASD keyboard teleoperation
* Custom G1 12-DOF robot description
* URDF and MuJoCo XML models
* Custom deployment configuration
* Foundation for future LiDAR, SLAM, and autonomous navigation development

The project is currently under active development.

---

## ✨ Current Features

* ✅ G1 12-DOF robot model
* ✅ MuJoCo simulation
* ✅ WASD keyboard teleoperation
* ✅ Forward and backward movement
* ✅ Left and right movement
* ✅ Custom robot configuration
* ✅ Custom URDF model
* ✅ Custom MuJoCo XML model
* 🔄 LiDAR integration and development
* 🔄 SLAM development
* 🔄 Autonomous navigation

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
└── src/
    └── g1_description/
        ├── g1_12dof.urdf
        └── g1_12dof.xml
```

### Key Files

| File                              | Description                                        |
| --------------------------------- | -------------------------------------------------- |
| `g1_12dof_wasd.py`                | Main 12-DOF G1 MuJoCo teleoperation script         |
| `g1_12dof_wasd_WORKING_BACKUP.py` | Backup of the working teleoperation implementation |
| `g1.yaml`                         | G1 deployment and simulation configuration         |
| `g1_12dof.xml`                    | MuJoCo model description                           |
| `g1_12dof.urdf`                   | URDF robot description                             |

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

---

## 🔗 Base Framework

G1 Mark 1 is developed using the **Unitree RL Gym framework** as the underlying robotics and reinforcement-learning environment.

The original framework is available here:

**Official Unitree RL Gym Repository**

https://github.com/unitreerobotics/unitree_rl_gym

This repository contains the **custom G1 Mark 1 development work** built on top of the underlying framework.

---

## ⚙️ Setup

Clone the official Unitree RL Gym framework:

```bash
git clone https://github.com/unitreerobotics/unitree_rl_gym.git
```

Enter the framework directory:

```bash
cd unitree_rl_gym
```

Activate your Python environment:

```bash
source ~/g1_rl_env/bin/activate
```

Clone or copy the G1 Mark 1 project files into the corresponding directories of the Unitree RL Gym environment.

---

## 🎮 Running G1 Mark 1

After setting up the Unitree RL Gym environment and placing the G1 Mark 1 files in the appropriate locations, run:

```bash
cd ~/unitree_rl_gym
```

Activate the environment:

```bash
source ~/g1_rl_env/bin/activate
```

Run the 12-DOF G1 WASD teleoperation:

```bash
PYTHONPATH=$PWD python deploy/deploy_mujoco/g1_12dof_wasd.py g1.yaml
```

The G1 humanoid robot will launch in the MuJoCo simulation environment.

---

## 🎮 Teleoperation

The G1 Mark 1 system supports keyboard-based teleoperation using the WASD control interface.

| Key | Action        |
| --- | ------------- |
| `W` | Move Forward  |
| `S` | Move Backward |
| `A` | Move Left     |
| `D` | Move Right    |

Additional controls may depend on the current implementation of the teleoperation script.

---

## 🧠 Development Roadmap

The project is under active development.

### Completed

* [x] G1 12-DOF robot model
* [x] MuJoCo simulation
* [x] WASD teleoperation
* [x] Custom deployment configuration
* [x] Custom URDF and MuJoCo XML models

### In Development

* [ ] LiDAR integration
* [ ] SLAM implementation
* [ ] Map generation improvements
* [ ] Autonomous navigation
* [ ] ROS 2 integration
* [ ] Navigation and path planning
* [ ] Extended humanoid autonomy

---

## 📌 Project Status

**Current Status:** Active Development

**Current Milestone:** G1 Mark 1 — Working 12-DOF Humanoid Robot WASD Teleoperation

The current focus is on improving the robot simulation, sensor integration, SLAM capabilities, and autonomous navigation pipeline.

---

## 👨‍💻 Author

**Jeeva Anthrose S**

Robotics & Automation Engineer

Focused on:

* Robotics
* Humanoid Robots
* Autonomous Systems
* ROS 2
* SLAM
* Computer Vision
* AI & Machine Learning
* Embedded Systems

---

## 📜 Acknowledgements

This project builds upon the work and framework provided by **Unitree Robotics** and the open-source robotics community.

Special reference:

**Unitree RL Gym**

https://github.com/unitreerobotics/unitree_rl_gym

The original framework and its respective licenses and attributions belong to their respective authors.

---

## 📄 License

This project contains custom development work by the author and is built upon external open-source frameworks.

Please refer to the original Unitree RL Gym repository and its license for the underlying framework:

https://github.com/unitreerobotics/unitree_rl_gym
