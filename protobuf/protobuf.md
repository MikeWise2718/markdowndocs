---
title: "Protocol Buffers (protobuf)"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Googles Json.


# Links
- short example - <https://stackoverflow.com/a/43875180/3458744>
- Tutorial - <https://developers.google.com/protocol-buffers/docs/tutorials>
- Some warts - <https://github.com/protocolbuffers/protobuf/issues/3028>

# Samples

Version 2
```
syntax = "proto2";

package tutorial;

message Person {
  required string name = 1;
  required int32 id = 2;
  optional string email = 3;

  enum PhoneType {
    MOBILE = 0;
    HOME = 1;
    WORK = 2;
  }

  message PhoneNumber {
    required string number = 1;
    optional PhoneType type = 2 [default = HOME];
    }
     repeated PhoneNumber phones = 4;
  }

message AddressBook {
   repeated Person people = 1;
}
```

Version 3
```
 syntax = "proto3";

 package tutorial;

  message Person {
    string name = 1;
    int32 id = 2;
    string email = 3;
 
   enum PhoneType {
     MOBILE = 0;
     HOME = 1;
     WORK = 2;
   }
 
   message PhoneNumber {
     string number = 1;
     PhoneType type = 2;
   }
 
   repeated PhoneNumber phones = 4;
 }
 message AddressBook {
   repeated Person people = 1;
 }
```


Using it
```
#! /usr/bin/python

import addressbookv2_pb2
import sys

# This function fills in a Person message based on user input.
def PromptForAddress(person):
  person.id = int(raw_input("Enter person ID number: "))
  person.name = raw_input("Enter name: ")

  email = raw_input("Enter email address (blank for none): ")
  if email != "":
    person.email = email

  while True:
    number = raw_input("Enter a phone number (or leave blank to finish): ")
    if number == "":
      break

    phone_number = person.phones.add()
    phone_number.number = number

    type = raw_input("Is this a mobile, home, or work phone? ")
    if type == "mobile":
      phone_number.type = addressbookv2_pb2.Person.MOBILE
    elif type == "home":
      phone_number.type = addressbookv2_pb2.Person.HOME
    elif type == "work":
      phone_number.type = addressbookv2_pb2.Person.WORK
    else:
      print "Unknown phone type; leaving as default value."

# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
  sys.exit(-1)

address_book = addressbookv2_pb2.AddressBook()

# Read the existing address book.
try:
  f = open(sys.argv[1], "rb")
  address_book.ParseFromString(f.read())
  f.close()
except IOError:
  print sys.argv[1] + ": Could not open file.  Creating a new one."

# Add an address.
PromptForAddress(address_book.people.add())

# Write the new address book back to disk.
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
```

# Commands
Compile a proto into source code (python and c-sharp)
```
#!/bin/bash
protoc -I=. --python_out=. ./addressbookv2.proto
protoc -I=. --csharp_out=. ./addressbookv3.proto
```


Run it and convert the binary protobuf file to protbuf text
```
!#/bin/bash
python testpython1.py afile.pb
protoc --decode_raw < afile.pb >afileraw.pbtxt
protoc --decode tutorial.AddressBook addressbookv2.proto < afile.pb >afile.pbtxt
```

`afile.pb`
```

mike@Abra:~/tfrepos/protoc$ hd afile.pb
00000000  0a 25 0a 04 6d 69 6b 65  10 0c 1a 0d 6d 69 6b 65  |.%..mike....mike|
00000010  40 6d 61 69 6c 2e 63 6f  6d 22 0c 0a 08 31 32 33  |@mail.com"...123|
00000020  2d 34 35 36 37 10 01                              |-4567..|
00000027
```

`afileraw.pbtxt` - `protoc --decode_raw < afileraw.pb`
```
1 {
  1: "mike"
  2: 12
  3: "mike@mail.com"
  4 {
    1: "123-4567"
    2: 1
  }
}
```

`afile.pbtxt` - `protoc --decode tutorial.AddressBook addressbookv2.proto < afile.pb`
```
people {
  name: "mike"
  id: 12
  email: "mike@mail.com"
  phones {
    number: "123-4567"
    type: HOME
  }
}
```

# Tensorflow protobuf stuff

- Very weak documentation - <https://www.tensorflow.org/extend/tool_developers/>
- Had to add `/home/mike/tfrepos/google/protobuf/any.proto`
`protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode GraphDef /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/meta_graph.proto <  /home/mike/tfrepos/tbex_mnist/export/1/saved_model.pb`
`protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode MetaGraphDef /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/meta_graph.proto <  /home/mike/tfrepos/models/research/export/Servo_0/1539552921/saved_model.pb`

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
(tf27gpu) mike@Abra:~/tfrepos/tbex_mnist/export/1/variables$protoc  --proto_path=/home/mike/tfrepos/tf11_cp27/ --decode tensorflow.SavedModel /home/mike/tfrepos/tf11_cp27/tensorflow/core/protobuf/saved_model.proto <  saved_model.pb 

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