---
title: "Isaac Labs"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Derived from Isaac Orbit

# IsaacLab 1.X

## Install
- Instructions here: ()
- `git clone https://github.com/isaac-sim/IsaacLab.git`
- `cd IsaacLab`
- `isaaclab.bat --help`
- The following needs an admin console
- `mklink /D _isaac_sim C:\Users\mwise\AppData\Local\ov\pkg\isaac-sim-4.0.0`
- `isaaclab.bat --install`


## Verification
- Existing scripts (samples): (https://isaac-sim.github.io/IsaacLab/source/setup/sample.html)
- Example:
   - `isaaclab.bat -p source/standalone/demos/quadrupeds.py`  - takes like 90 seconds to load so be patient with the black Isaac Sim screen

# IsaacLab 2.0 - Jan 2025
## Install
- Instructions here: (https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/isaaclab_pip_installation.html)

## Install Commands
- `git clone https://github.com/isaac-sim/IsaacLab.git`
- `cd IsaacLab`
- `sudo apt install python3.10-venv`
- `python3.10 -m venv env_isaaclab`
- `source env_isaaclab/bin/activate`
- `pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu121`
- `pip install 'isaacsim[all,extscache]==4.5.0' --extra-index-url https://pypi.nvidia.com`
- `./isaaclab.sh --help`
- `sudo apt install cmake build-essential`
- `./isaaclab.sh --install`

## Verify
- `./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py`

## See all the possible environments
- `./isaaclab.sh -p scripts/environments/list_envs.py`

## A real test run
-  Remove `--headless` parameter from the following if you want to watch it execute, but it will go much much slower
- `./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Ant-v0 --headless` (took like 600 seconds on a 4070)

## Understanding PPO
- Medium article: https://medium.com/@chris.p.hughes10/understanding-ppo-a-game-changer-in-ai-decision-making-explained-for-rl-newcomers-913a0bc98d2b


# Isaac Gym
- Depreciated, but still lots of good things there
- Install article on Medium:(https://medium.com/@piliwilliam0306/install-isaac-gym-on-ubuntu-22-04-8ebf4b86e6f7)
- LD_LIBRARY Fix:
   - `find . --name libsomethingorother`
   - `export LD_LIBRARY_PATH=/home/mike/miniconda3/pkgs/python-3.7.12-hf930737_100_cpython/lib/`
   - apparently you can do an `apt install libpython3.7` but it didn't work for me
   - `sudo apt install mk
- Video on Legged Demo: (https://www.youtube.com/watch?v=02euh9dC2tw)
- Legged Demo repo: (https://github.com/leggedrobotics/legged_gym)