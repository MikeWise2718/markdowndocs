---
title: "Unity3D"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Unity ml-agents is an RL framework for Unity that is quite powerful - and a lot of fun.
- It has been out for a couple of years, and there is a wealth of information on it available. 
- The downloadable SDK has 10 example implementations and we will be using the “Push Block” tutorial  to base our hackathon on as it has most of the features we will need (notably a ray based environment sensing setup). 
- The SDK can be found here: (https://github.com/Unity-Technologies/ml-agents)
- This tutorial is a good place to start as it goes over the PushBlock example:
(https://www.youtube.com/playlist?list=PLX2vGYjWbI0R08eWQkO7nQkGiicHAX7IX)

You can follow it along with a newer version of Unity and the current ml-agents, however note that the tutorial is over a year old and uses a different version, so some of the code and Editor controls are not quite the same.


# Install and run a test training session:
-	Install `ml-agents` (see link below)
-	Start an Anaconda DOS prompt
-	Start the Unity example that you want to test (like pushblock)
-	Load a scene with an academy in it 
-	Make sure the agents are configured with a learning brain (and not a player brain)
-	Make sure the academy is configured with a learning brain 
-	`activate ml-agents`
-	`cd d:\unity\mlagents`
-	`mlagents-learn config/trainer_config.yaml  -–train --run-id=something_1 `
-	It will emit a bunch of messages and then ask you to "Hit Play" in the Unity Editor
-   Training will run the number of steps configured in `trainer_config.yaml`
-   After the run is finished (or interrrupted) the trained brain should be in:
    - `unity/ml-agents/models/<run-identifier>/<brain_name>.nn`
-   To use in your app copy it to the `Assets/../TFmodels` folder and configure it into your player brain


# Training a brain and installing it end-to-end
- Here: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Basic-Guide.md)

# Training code
- It is compiled, probably with `py2exe`
- But you can run the python directly:
    - `cd unity/ml-agents`
    - `python3 ml-agents/mlagents/trainers/learn.py config/trainer_config.yaml  -–train --run-id=something_1` 
    - The way to do it is to create a subclass of `Trainer`, similar to `PPOTrainer`
    - `class Trainer` is in  `trainer.py` and `class PPOTrainer` is in `ppo/trainer.py` which is a bit confusing

# Code Structure
- Code is in `ml-agents/ml-agents`
- There is a `README.md` there worth reading: (https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents)
- There are two sub-packagtres
   -  `mlagents.env` a low-level PAPI to talk to Unity 
   -  `mlagents.trainers` A set of RL learning algorithms that works with the above

## mlagents.env
- code in `ml-agents/ml-agent-envs`
- There is a readme there too: (https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents-envs)
- Can apparently be installed on its own
- Data transported to Unity and back in `ml-agents/ml-agents-envs/mlagents/envs/brain.py`



## Steps to generalizing an SDK example
-   Opened the UnitySDK project
-	Copyied Hallway Example `Assets/ML-Agents/Examples/Hallway` over to a new folder `Assets/ML-Agents/Examples/CrowdMove`
-	Renamed `HallwayLearning` Scene to `CrowdMoveLearning` and deleted the other scenes
-	Renamed the `HallwayLearning` brain to `CrowdMoveLearning` brain
-	Renamed the `HallwayLearning` TFmodel to `CrowdMoveLearning` TFmodel
-	Created new Scripts `CrowdMoveAcademy` and `CrowdMoveAgent` by renaming the `.cs` files and renaming the class names – and then deleted the old ones
-	Renamed `HallwayAcademy` GameObject in Hierarchy view to `CrowdMoveAcademy`, deleted the `HallwallAcademy` component in it, and added the new `CrowdMoveAcademy` component
-	Renamed the `HallwayArea` Prefab to `CrowdMovearea` Prefab and deleted the `HallwayAgent` component in the `Agent` GameObjec and added the `CrowdMoveAgent` Component
-	Deleted all 16 `HallwayArea` prefab instances from `CrowdMoveLearning` scene and added a single `CrowdMoveArea` Prefab instance (for now only want one)
-	Assigned all the local GameObject reference variables (6 of them) in the `CloudMoveAgent` component in the prefab. They pointed at other GameOjects in the prefab
-	Assigned the `CrowdMoveLearning` brain to the `CrowdMoveAgent` component in the prefab
-	Checked the `Use Vector Obs` checkbox in the `CrowdMoveAgent` component in the prefab
-   Checked the variable values in the `CrowdMoveAcademy` to see if they were the same as the `HallwayAcademy` prefab. They weren't....
   - Did this by screenshoting `HallwayAcademy` component settings and hand copied them into `CrowdMoveAcademy` component
-	Added `CrowdMoveLearning` TFmodel to `CrowdMoveLearning` brain (initializes empty)
-	Changed 2 lines of code Initialization routine in `CrowMoveAgent` Script to:
     - `CrowdMoveAcademy academy;`
     - `academy = FindObjectOfType<CrowdMoveAcademy>();`  
-	Added `CrowdMoveLearning` Brain to Broadcast Hub in `CrowdMoveAcademy` component and checked Control checkbox
-	Make sure `Control` checkbox is ticked in `CrowdMoveAcademy` component or you will get a timeout when you start the learn python script and some useless suggestions on how to fix it
-   It worked .... may have forgotten to document a step or two here though

# Tensorboard
- Explained here: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Using-Tensorboard.md)
- The essential bit
```
The ML-Agents toolkit saves statistics during learning session that you can view with a TensorFlow utility named, TensorBoard.

The mlagents-learn command saves training statistics to a folder named summaries, organized by the run-id value you assign to a training session.

In order to observe the training process, either during training or afterward, start TensorBoard:

1. Open a terminal or console window:

2. Navigate to the directory where the ML-Agents Toolkit is installed (cloned to - e.g. `~/Unity/ml-agents`)

3. From the command line run :
      tensorboard --logdir=summaries

4. Open a browser window and navigate to localhost:6006.

Note: If you don't assign a run-id identifier, mlagents-learn uses the default string, "ppo". All the statistics will be saved to the same sub-folder and displayed as one session in TensorBoard. After a few runs, the displays can become difficult to interpret in this situation. You can delete the folders under the summaries directory to clear out old statistics.
```
- worked without problem from my windows host remotely `http://192.168.25.12:6006` - seems like it should not have?
### To Add Observations
- The `custom_observations` field in `Brain_info` seems to be appropriate for this 
- Docs are here: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Creating-Custom-Protobuf-Messages.md)
- You have to declare the data in protobuf, then compile to get the C# and Python code 
- Protobuf files found in: `D:\Unity\ml-agents\protobuf-definitions\proto\mlagents\envs\communicator_objects` (`dir /s *.proto`)
- Seems to be that PPO does not use `custom_observations` in training (`D:\Unity\ml-agents\ml-agents\mlagents\trainers\ppo\trainer.py` does not reference it)
- Need to add field to stats and see if it comes over in the above `ppo\trainer.py` file
- To do:
   - Add field to stats in `ppo/trainer.py` and append dummy data to it every step
   - See if it displays
   - Change the dummy data to be something from the observations
   - See if it displays
   - Add a custom_observation field and compile it
   - Populate it from Unity and see if it comes over
   - Then use it


## More Links
- Installing ml-agents on Windows: `https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation-Windows.md
- ml-agents GitHub repo: https://github.com/Unity-Technologies/ml-agents
- ml-agents Documentation: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Readme.md
- Unity ml-agents at GDC 2018: https://www.youtube.com/watch?v=YsEDv13W1RI
- Proximal Policy Optimization: https://arxiv.org/pdf/1707.06347.pdf
- PushBlock Tutorial: https://www.youtube.com/playlist?list=PLX2vGYjWbI0R08eWQkO7nQkGiicHAX7IX
- Vision Zero, Uni Barcelona and Bellevue: https://www.youtube.com/watch?v=YsEDv13W1RI (37:38)

