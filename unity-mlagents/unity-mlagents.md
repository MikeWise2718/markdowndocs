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


Install and run:
-	Install ml-agents (see link below)
-	Start an Anaconda DOS prompt
-	Start the Unity example that you want to test (like pushblock)
-	Load a scene with an academy in it 
-	Make sure the agents are configured with a learning brain (and not a player brain)
-	Make sure the academy is configured with a learning brain 
-	`activate ml-agents`
-	`cd d:\unity\mlagents`
-	`mlagents-learn config/trainer_config.yaml  --run-id=smth_1 –train`
-	It will emit a bunch of messages and then ask you to "Hit Play" in the Unity Editor


## More Links
- Installing ml-agents on Windows: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation-Windows.md
- ml-agents GitHub repo: https://github.com/Unity-Technologies/ml-agents
- ml-agents Documentation: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Readme.md
- Unity ml-agents at GDC 2018: https://www.youtube.com/watch?v=YsEDv13W1RI
- Proximal Policy Optimization: https://arxiv.org/pdf/1707.06347.pdf
- PushBlock Tutorial: https://www.youtube.com/playlist?list=PLX2vGYjWbI0R08eWQkO7nQkGiicHAX7IX
- Vision Zero, Uni Barcelona and Bellevue: https://www.youtube.com/watch?v=YsEDv13W1RI (37:38)

