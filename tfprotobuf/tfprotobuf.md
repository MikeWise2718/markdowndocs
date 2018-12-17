---
title: "TensorFlow Protocol Buffers"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Tensorflow protobuf stuff
For general - i.e. not tensorflow related -  protobuf notes see my protobuf notes

# Tensorflow protobuf stuff
- Trolling for protobufs in tensorflow source - From `~/tfrepos/tf11_cp27$` do `grep -ri syntax --include='*.proto'` - We got 111 hits, so there are 111 proto files
- Some rather weak documentation - <https://www.tensorflow.org/extend/tool_developers/>
`protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.SavedModel /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/saved_model.proto <  /home/mike/tfrepos/models/research/export/Servo_0/1539552921/saved_model.pb`

- <https://stackoverflow.com/questions/21159451/protobuffs-import-from-another-directory>
- <https://stackoverflow.com/questions/51233023/extract-graph-def-from-model-ckpt-meta>
- <https://stackoverflow.com/questions/34343259/is-there-an-example-on-how-to-generate-protobuf-files-holding-trained-tensorflow>
- <https://tensorflow.github.io/haskell/haddock/tensorflow-proto-0.2.0.0/Proto-Tensorflow-Core-Protobuf-MetaGraph.html>
- tf.train.write_graph - <https://www.tensorflow.org/api_docs/python/tf/train/write_graph>
- <https://stackoverflow.com/questions/49198493/tensorflow-how-to-compare-2-checkpoints>
- <https://stackoverflow.com/questions/45864363/tensorflow-how-to-convert-meta-data-and-index-model-files-into-one-graph-pb>


# Saved Model
- Code and protobuf described here: <https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/saved_model>
- Useful post - <http://www.seaandsailor.com/tensorflow-checkpointing.html>
- related - <https://stackoverflow.com/questions/38829641/tensorflow-train-import-meta-graph-does-not-work>
- checkpoint files appear not to be protobuf files as they have too many zeros in them - but of cours I am not sure
   - <https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/session_bundle>
- How to freeze a graph according to reddit <https://www.reddit.com/r/tensorflow/comments/6xhjpb/how_to_convert_checkpoint_files_to_pb_file/>
- <https://stackoverflow.com/questions/48701666/save-tensorflow-checkpoint-to-pb-protobuf-file>

Hre we dump a saved_model saved with the model builder which saves it as a tensorflow.SavedModel protobuf
```
(tf27gpu) mike@Abra:~/tfrepos/tbex_mnist/export/1$protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.SavedModel /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/saved_model.proto <  saved_model.pb 

saved_model_schema_version: 1
meta_graphs {
  meta_info_def {
    stripped_op_list {
      op {
        name: "Add"
        input_arg {
          name: "x"
          type_attr: "T"
        }
        input_arg {
          name: "y"
          type_attr: "T"
        }
        output_arg {
          name: "z"
          type_attr: "T"
        }
        attr {
          name: "T"
          type: "type"
          allowed_values {
            list {
              type: DT_BFLOAT16
              type: DT_HALF
              type: DT_FLOAT
              type: DT_DOUBLE
              type: DT_UINT8
              type: DT_INT8
              type: DT_INT16
              type: DT_INT32
              type: DT_INT64
              type: DT_COMPLEX64
              type: DT_COMPLEX128
              type: DT_STRING
            }
          }
        }
      }
      op {
        name: "ApplyGradientDescent"
        input_arg {
....
and more...
```

frozen inference graphs are different - tensrorflow.GraphDef protobuf.
```
protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.GraphDef /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/saved_model.proto <  frozen_inference_graph.pb 
node {
  name: "image_tensor"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_UINT8
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: -1
        }
        dim {
          size: -1
        }
        dim {
          size: -1
        }
        dim {
          size: 3
        }
      }
    }
  }
}
node {
  name: "ToFloat"
  op: "Cast"
  input: "image_tensor:0"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_UINT8
    }
  }
}

```


Not convinced the checkpoint stuff is not a protodef, but these fail - were referenced in saver.py <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/training/saver.py>:
```
(tf27gpu) mike@Abra:~/tfrepos/tbex_mnist/export2/1/variables$ protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.MetaGraphDef /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/meta_graph.proto <  variables.data-00000-of-00001
Failed to parse input.
(tf27gpu) mike@Abra:~/tfrepos/tbex_mnist/export2/1/variables$ protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.Saver /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/saver.proto <  variables.data-00000-of-00001
Type not defined: tensorflow.Saver
(tf27gpu) mike@Abra:~/tfrepos/tbex_mnist/export2/1/variables$ protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.SaverDef /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/saver.proto <  variables.data-00000-of-00001
Failed to parse input.
(tf27gpu) mike@Abra:~/tfrepos/tbex_mnist/export2/1/variables$

```