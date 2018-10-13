---
title: "Tensorflow Object Detection Zoo"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

![TensorFlow logo](tflogo.png)

# Intro
- Also known as the Object Detection API link: <https://github.com/tensorflow/models/tree/master/research/object_detection>
- A good post on building and training the model <https://stackoverflow.com/questions/44973184/train-tensorflow-object-detection-on-own-dataset/44973203#44973203>


# tensorflow logging
  - my wonderful post: https://stackoverflow.com/questions/44853059/tensorflow-logging-messages-do-not-appear/49756653#49756653 

 # tensorflow object detection zoo models on abra
  - These are the github google Tensorflow models found [here](https://github.com/tensorflow/models/tree/master/research/object_detection)
  - Clone all the models into a directory `git clone https://github.com/tensorflow/models`
  - Change to home dir `cd ~`
  - Activete the right environment for python `source ./tf27gpu/bin/activate`
  - now go to the object detection directory `cd ~/tfrepos/models/research/object_detection`
  - Start jupyter on the right notebook `jupyter notebook object_detection_tutorial.ipynb`
  - If you get error "could not create cudnn handle: CUDNN_STATUS_NOT_INITIALIZED" try the following
  - Start jupyter on the right notebook `sudo jupyter notebook object_detection_tutorial.ipynb --allow-root`

# Issues
  - Installing on Windows - you need to install "Protocol Buffers" Googles datae handling protocol `protobuf` first, which has to be compiled from source
     - https://github.com/google/protobuf 
  - On ubuntu the `arial.ttf` font is not installed by default. See this:   
    - https://stackoverflow.com/a/50006012/3458744 


# Training a new model
- Described fairly well in this answer: <https://stackoverflow.com/questions/44973184/train-tensorflow-object-detection-on-own-dataset/44973203#44973203>
- 


# zoo Object Ids

```
  ## Loading label map
  PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')
  label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
  categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
  for ii in range({NUM_CLASSES):
      print(categories[ii])
      category_index = label_map_util.create_category_index(categories)
      print(category_index)



{'name': 'person', 'id': 1}
{'name': 'bicycle', 'id': 2}
{'name': 'car', 'id': 3}
{'name': 'motorcycle', 'id': 4}
{'name': 'airplane', 'id': 5}
{'name': 'bus', 'id': 6}
{'name': 'train', 'id': 7}
{'name': 'truck', 'id': 8}
{'name': 'boat', 'id': 9}
{'name': 'traffic light', 'id': 10}
{'name': 'fire hydrant', 'id': 11}
{'name': 'stop sign', 'id': 13}
{'name': 'parking meter', 'id': 14}
{'name': 'bench', 'id': 15}
{'name': 'bird', 'id': 16}
{'name': 'cat', 'id': 17}
{'name': 'dog', 'id': 18}
{'name': 'horse', 'id': 19}
{'name': 'sheep', 'id': 20}
{'name': 'cow', 'id': 21}
{'name': 'elephant', 'id': 22}
{'name': 'bear', 'id': 23}
{'name': 'zebra', 'id': 24}
{'name': 'giraffe', 'id': 25}
{'name': 'backpack', 'id': 27}
{'name': 'umbrella', 'id': 28}
{'name': 'handbag', 'id': 31}
{'name': 'tie', 'id': 32}
{'name': 'suitcase', 'id': 33}
{'name': 'frisbee', 'id': 34}
{'name': 'skis', 'id': 35}
{'name': 'snowboard', 'id': 36}
{'name': 'sports ball', 'id': 37}
{'name': 'kite', 'id': 38}
{'name': 'baseball bat', 'id': 39}
{'name': 'baseball glove', 'id': 40}
{'name': 'skateboard', 'id': 41}
{'name': 'surfboard', 'id': 42}
{'name': 'tennis racket', 'id': 43}
{'name': 'bottle', 'id': 44}
{'name': 'wine glass', 'id': 46}
{'name': 'cup', 'id': 47}
{'name': 'fork', 'id': 48}
{'name': 'knife', 'id': 49}
{'name': 'spoon', 'id': 50}
{'name': 'bowl', 'id': 51}
{'name': 'banana', 'id': 52}
{'name': 'apple', 'id': 53}
{'name': 'sandwich', 'id': 54}
{'name': 'orange', 'id': 55}
{'name': 'broccoli', 'id': 56}
{'name': 'carrot', 'id': 57}
{'name': 'hot dog', 'id': 58}
{'name': 'pizza', 'id': 59}
{'name': 'donut', 'id': 60}
{'name': 'cake', 'id': 61}
{'name': 'chair', 'id': 62}
{'name': 'couch', 'id': 63}
{'name': 'potted plant', 'id': 64}
{'name': 'bed', 'id': 65}
{'name': 'dining table', 'id': 67}
{'name': 'toilet', 'id': 70}
{'name': 'tv', 'id': 72}
{'name': 'laptop', 'id': 73}
{'name': 'mouse', 'id': 74}
{'name': 'remote', 'id': 75}
{'name': 'keyboard', 'id': 76}
{'name': 'cell phone', 'id': 77}
{'name': 'microwave', 'id': 78}
{'name': 'oven', 'id': 79}
{'name': 'toaster', 'id': 80}
{'name': 'sink', 'id': 81}
{'name': 'refrigerator', 'id': 82}
{'name': 'book', 'id': 84}
{'name': 'clock', 'id': 85}
{'name': 'vase', 'id': 86}
{'name': 'scissors', 'id': 87}
{'name': 'teddy bear', 'id': 88}
{'name': 'hair drier', 'id': 89}
{'name': 'toothbrush', 'id': 90}
```