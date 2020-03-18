---
title: "Unity3D"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Unity ml-agents is an Open Source (Apache License) RL framework for Unity that is quite powerful - and a lot of fun.
- Web site is github site (https://github.com/Unity-Technologies/ml-agents)
- It has been out for a couple of years, and there is a wealth of information on it available. 
- The downloadable SDK has 10 example implementations and we will be using the “Push Block” tutorial  to base our hackathon on as it has most of the features we will need (notably a ray based environment sensing setup). 
- The SDK can be found here: (https://github.com/Unity-Technologies/ml-agents)
- Docs: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Readme.md)
- This tutorial is a good place to start as it goes over the PushBlock example:
(https://www.youtube.com/playlist?list=PLX2vGYjWbI0R08eWQkO7nQkGiicHAX7IX)
- mlagents 0.11.0 implenets two algorithems, PPO and SAC
 

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
-  `pip freeze | grep mlagents` currently idenfities version as `0.11.0` (17 Nov 2019)
# Training a brain and installing it end-to-end
- Here: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Basic-Guide.md)

# Training code
- It is compiled, probably with `py2exe`
- But you can run the python directly:
    - `cd unity/ml-agents`
    - `python3 ml-agents/mlagents/trainers/learn.py config/trainer_config.yaml  -–train --run-id=something_1` 
    - The way to do it is to create a subclass of `Trainer`, similar to `PPOTrainer`
    - `class Trainer` is in  `trainer.py` and `class PPOTrainer` is in `ppo/trainer.py` which is a bit confusing

# Python Code Structure
- Code is in `ml-agents/ml-agents`
- There is a `README.md` there worth reading: (https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents)
- There are two sub-packagtres
   -  `mlagents.env` an API that exchanges environment information with Unity using protobuf  
   -  `mlagents.trainers` A set of RL learning algorithms that works with the above
- If you want to run that code, you have to make sure the PYTHONPATH points.
   - Otherwise it will pick up the modules you installed with `pip`
   - You can find out what module is being used for an open using the `inspect` module - see below<br>

Examples:
```
(ml-agents) D:\Unity\ml-agents>env | grep PYTHONPATH
PYTHONPATH=d:\Unity\ml-agents\ml-agents;d:\Unity\ml-agents\ml-agents-envs;
```
```
print(f"PythonPath:{os.environ.get('PYTHONPATH')}")

import types
def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__
print("imported modules:"+str(list(imports())))


import inspect
print("UnityEnvironment imported from :"+inspect.getfile(UnityEnvironment))
print("TrainerFactory imported from :"+inspect.getfile(TrainerFactory))
```


## mlagents.env
- code in `ml-agents/ml-agent-envs`
- There is a readme there too: (https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents-envs)
- Can apparently be installed on its own
- Data transported to Unity and back in `ml-agents/ml-agents-envs/mlagents/envs/rpc_communicator.py` in the    `exchange` function
- Can't be easily debugged because it is 

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

# Restarting Training
- Here is a discussion:(https://github.com/Unity-Technologies/ml-agents/issues/532)
- Basically just use `--load` as in: `python learn.py name --run-id=13 --train --load` 
- `run-id` has to be the same of course, `Step:` count will continue from interruption but `Time Elapsed:` will reset tp zero
- Here is a more involved one:(https://github.com/Unity-Technologies/ml-agents/issues/138
)

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

### To Add Observations (obsolete)
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

# Notes on adding tensorboard observations
- Data comes in through protobuf
## Protobuf

### Protobuf chanegs
Only had to add one and change one protbuf file 
- Defintions in  `/ml-agents/protobuf-definitions/proto/mlagents/envs/communicator_objects ml-agents/protobuf_definitions`)
- New file: `environment_statistics.proto`
### Compile things
- Have to compile the new protobuf definitions and get them to work, which is painful
- Look at the `README.md` in the `/ml-agents/protobuf-definitions` directory to find the version of Grpc tools you need (in this case 1.14.1)
- Installation: `nuget install Grpc.Tools -Version 1.14.1 -OutputDirectory $MLAGENTS_ROOT\protobuf-definitions`
   - I used `nuget install Grpc.Tools -Version 1.14.1 -OutputDirectory .`
- Afterwards the `COMPILER` variable in the `make_for_win.bat` had to point to the Grpc Tools directory, wherever it was installed 
   -  I installed it in a the same directory which is probably not optimal
   - `set COMPILER=D:\Unity\ml-agents\protobuf-definitions\Grpc.Tools.1.14.1\tools\windows_x64`
- Then compile with the `make_for_win.bat` - you have to look carefully to find the errors in the output
- Afterwards you should be able have `EnvironmentStatisticsProto` be a known type in `RpcCommunicator.cs`, just like `UnityOutputProto` is by default

```
syntax = "proto3";

option csharp_namespace = "MLAgents.CommunicatorObjects";
package communicator_objects;

message EnvironmentStatisticsProto {
    map<string, float> float_stat = 1; 
    map<string, string> string_stat = 2; 
}
```
- changed file:  `unity_rl_outout.proto`
```
syntax = "proto3";

import "mlagents/envs/communicator_objects/agent_info.proto";
import "mlagents/envs/communicator_objects/environment_statistics.proto";

option csharp_namespace = "MLAgents.CommunicatorObjects";
package communicator_objects;

message UnityRLOutputProto {
    message ListAgentInfoProto {
        repeated AgentInfoProto value = 1;
    }
    reserved 1; // deprecated bool global_done field
    map<string, ListAgentInfoProto> agentInfos = 2;
    EnvironmentStatisticsProto environment_statistics = 3;
}
```


## C#
- Added file `EnvStatMan.cs` to `UnitySDK\Assets\ML-Agents\Scripts`
```
using System;
using UnityEngine;
using System.Collections.Generic;
using Google.Protobuf.Collections;

namespace MLAgents
{
    public class EnvStatMan
    {
        Dictionary<string, float> floatStat;
        Dictionary<string, string> stringStat;
        public EnvStatMan()
        {
            Reset();
        }
        public void Reset()
        {
            floatStat = new Dictionary<string, float>();
            stringStat = new Dictionary<string, string>();
        }
        static string tbprefix = "tb:";
        public void AddFloatStat(string key,float valf)
        {
            floatStat[tbprefix+key] = valf;
        }
        public void AddStringStat(string key, string vals)
        {
            stringStat[key] = vals;
        }
        public void FillFloatMapField(MapField<string,float> mapfield)
        {
            foreach( var k in floatStat.Keys)
            {
                mapfield[k] = floatStat[k];
            }
        }
        public void FillStringMapField(MapField<string, string> mapfield)
        {
            foreach (var k in stringStat.Keys)
            {
                mapfield[k] = stringStat[k];
            }
        }
    }
}
```

in `Academy.cs`
```
    public abstract class Academy : MonoBehaviour
    {
        private const string k_ApiVersion = "API-11";

        /// Temporary storage for global gravity value
        /// Used to restore oringal value when deriving Academy modifies it
        private Vector3 m_OriginalGravity;

        /// Temporary storage for global fixedDeltaTime value
        /// Used to restore original value when deriving Academy modifies it
        private float m_OriginalFixedDeltaTime;

        /// Temporary storage for global maximumDeltaTime value
        /// Used to restore original value when deriving Academy modifies it
        private float m_OriginalMaximumDeltaTime;

        public EnvStatMan envStatMan = new EnvStatMan();
        // ...
```

in `Academy.cs`
```
        private void InitializeEnvironment()
        {
            m_OriginalGravity = Physics.gravity;
            m_OriginalFixedDeltaTime = Time.fixedDeltaTime;
            m_OriginalMaximumDeltaTime = Time.maximumDeltaTime;

            envStatMan.Reset();

            InitializeAcademy();
            // ...
```

in `RpcCommunicator.cs`
Initialization
```
        public UnityRLInitParameters Initialize(CommunicatorInitParameters initParameters)
        {
            var academyParameters = new UnityRLInitializationOutputProto
            {
                Name = initParameters.name,
                PackageVersion = initParameters.unityPackageVersion,
                CommunicationVersion = initParameters.unityCommunicationVersion
            };

            m_CurrentUnityRlOutput.EnvironmentStatistics = new EnvironmentStatisticsProto();
```

Per-step
```
        void SendBatchedMessageHelper()
        {
            var message = new UnityOutputProto
            {
                RlOutput = m_CurrentUnityRlOutput,
            };
            var tempUnityRlInitializationOutput = GetTempUnityRlInitializationOutput();
            if (tempUnityRlInitializationOutput != null)
            {
                message.RlInitializationOutput = tempUnityRlInitializationOutput;
            }
            EnvironmentStatisticsProto evo = message.RlOutput.EnvironmentStatistics;
            var aca = GameObject.FindObjectOfType<Academy>();
            aca.envStatMan.FillFloatMapField(evo.FloatStat);
            aca.envStatMan.FillStringMapField(evo.StringStat);
            aca.envStatMan.Reset();
            // ...
```



in `CmvAcademy.cs:`
```
    public override void AcademyStep()
    {
        envStatMan.AddFloatStat("CrowdMove/Attempts", attempts);
        envStatMan.AddFloatStat("CrowdMove/Successes", successes);
        envStatMan.AddFloatStat("CrowdMove/Failures", failures);
        envStatMan.AddFloatStat("CrowdMove/Collisions", collisions);
        envStatMan.AddFloatStat("CrowdMove/TotSteps", totsteps);
        envStatMan.AddFloatStat("CrowdMove/AvgSteps", avgsteps);
        if (timeDelayMsecs>0)
        {
            System.Threading.Thread.Sleep(timeDelayMsecs);
        }
    }
```
New Version <br>


In `FoodCollectorAgent.cs`

```
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("food"))
        {
            Satiate();
            collision.gameObject.GetComponent<FoodLogic>().OnEaten();
            AddReward(1f);
            if (contribute)
            {
                m_FoodCollecterSettings.totalScore += 1;
                m_FoodCollecterSettings.foodEaten += 1;
            }
        }
        if (collision.gameObject.CompareTag("badFood"))
        {
            Poison();
            collision.gameObject.GetComponent<FoodLogic>().OnEaten();

            AddReward(-1f);
            if (contribute)
            {
                m_FoodCollecterSettings.totalScore -= 1;
                m_FoodCollecterSettings.poisonEaten += 1;
            }
        }
    }
```
In `FoodCollectorSettings.cs`
```
public class FoodCollectorSettings : MonoBehaviour
{
    [HideInInspector]
    public GameObject[] agents;
    [HideInInspector]
    public FoodCollectorArea[] listArea;

    public int totalScore;
    public Text scoreText;

    public int foodEaten;
    public int poisonEaten;


    // ....


    public void FixedUpdate()
    {
        Academy.Instance.envStatMan.AddFloatStat("FoodCollector/TotalScore", totalScore);
        Academy.Instance.envStatMan.AddFloatStat("FoodCollector/FoodEaten", foodEaten);
        Academy.Instance.envStatMan.AddFloatStat("FoodCollector/PoisonEaten", poisonEaten);
    }
```

## Python ml-agents-env
- added `EnvStats` definition to `brain.py` line #27
```
class EnvStats:
    float_stat: Dict[str,float]
    string_stat: Dict[str,str]
    def __init__(
        self,
        float_stat:  Dict[str,float],
        string_stat: Dict[str,str],
    ):
        """
        Contains all EnvStats parameters.
        """
        self.float_stat = dict(float_stat)
        self.string_stat = dict(string_stat)

    def __str__(self):
        return f"float_stat:{self.float_stat} str_stat:{self.string_stat}"

    @staticmethod
    def from_proto(
        env_stat_proto: EnvironmentStatisticsProto
    ) -> "EnvStats":
        """
        Converts Environment Statistics parameter proto to EnvStats object.
        :param env_stat_proto: protobuf object.
        :return: EnvStats object.
        """
        env_stats = EnvStats(
            env_stat_proto.float_stat,
            env_stat_proto.string_stat,
        )
        return env_stats
```
- added following line to `UnityEnvironment._get_state` in `environment.py` lin3 #638
  - `_data["EnvStats"] = EnvStats.from_proto(self.env_stats)`
- added following line to `UnityEnvironment._update_brain_parameters` in `environment.py` lin3 #638
  - `self._env_stats = output.rl_output.environment_statistics`




# Starting a remote run on an DSVM
- Request Just-In-Time access to the box
- Login: `ssh mike@23.98.150.186`
- Start a detachable session (persistent screen) `screen` then return after the startup text
   - you can check it with `screen -r` now
- Activate the right Python Environment `source activate py36`
- Go to the directory: `cd ~/UnityProjects/ml_agents_modded`
- Start the script: `./run02`

run01:
```
#!/bin/bash
mlagents-learn config/trainer_config.yaml --train --run-id=dsvmrun01 --env=~/UnityProjects/m_agents_modded/UnitySDK/PMLbuild/rlsimple01.x86_64
```

# Tensorboard
- Docs: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Using-Tensorboard.md)
- Go to the directory: `cd ~/UnityProjects/ml_agents_modded`
- Start tensorboard `tensorboard --logdir=summaries`
- Go to azure portal and find the NSG (Network Security Group) associated with the VM (should have the same name+"_nsg")
- Add an inbound rule for port 6006 allowing everything
- Test using browser at `http://xxx.xxx.xxx.xxx:6006`

# Tensorboard - Custom Protobuf Messages
- Documented here: (https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Creating-Custom-Protobuf-Messages.md)
- ML-Agents Protobuf Definitions: (https://github.com/Unity-Technologies/ml-agents/blob/master/protobuf-definitions/README.md)

# More Links
- Installing ml-agents on Windows: `https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation-Windows.md
- ml-agents GitHub repo: https://github.com/Unity-Technologies/ml-agents
- ml-agents Documentation: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Readme.md
- Unity ml-agents at GDC 2018: https://www.youtube.com/watch?v=YsEDv13W1RI
- Proximal Policy Optimization: https://arxiv.org/pdf/1707.06347.pdf
- PushBlock Tutorial: https://www.youtube.com/playlist?list=PLX2vGYjWbI0R08eWQkO7nQkGiicHAX7IX
- Vision Zero, Uni Barcelona and Bellevue: https://www.youtube.com/watch?v=YsEDv13W1RI (37:38)


# Changes
- Got rid of `Academy` subclassing and what todo about it: (https://github.com/Unity-Technologies/ml-agents/pull/3184)
- `SpaceType` is now `ActionType` (although I think it is actually `ModelActionType`) : (https://github.com/Unity-Technologies/ml-agents/pull/3479)


# Essential Source Files Changed for custom-tb-origin

### Overview
Here is a summary of the important changes I had to do to get this to work

#### Protobuf changes:
- Added a new type to the protobuf defintions (**EnvironmentStatisticsProto**) to communicate data to the Python UnityEnvironment and merge it into **BatchedStepResult**. 
- Added **EnvironmentStatisticsProto** to **UnityRLOutputProto**

#### Python changes:
- Modified **base_env.py**, **rpc_utils.py**, and **environment.py** to read those.
- Modified **agent_processor.py** to pass those values to TensorBoard

#### C# Changes:
- Added a class to manage the collections **EnvStatMan.cs** in **com.unity.agents/Runtime**
- Made some minor modifications to **Academy.cs** and **RpcCommunication.cs** to integrate the **EnvStatMan** class into the RPC communicatino.
- Added a couple of counters (**foodEaten**, **poisonEaten**) to the **FoodCollectionSettings.cs**
- Added a FixedUpdate event handler to **FoodCollectionSettings.cs** to update those settings.

#### Other Changes
- There are a lot of little unimportant changes in this pull request that should not be there, but I am not sure how to quickly get rid of these so I am leaving them in for now. I think it is obvious what is signal and what is noise.
