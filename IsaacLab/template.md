---
title: "Isaac Labs"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Derived from Isaac Orbit

# Install
- Instructions here: ()
- `git clone https://github.com/isaac-sim/IsaacLab.git`
- `cd IsaacLab`
- `isaaclab.bat --help`
- The following needs an admin console
- `mklink /D _isaac_sim C:\Users\mwise\AppData\Local\ov\pkg\isaac-sim-4.0.0`
- `isaaclab.bat --install`


# Verification
- Existing scripts (samples): (https://isaac-sim.github.io/IsaacLab/source/setup/sample.html)
- Example:
   - `isaaclab.bat -p source/standalone/demos/quadrupeds.py`  - takes like 90 seconds to load so be patient with the black Isaac Sim screen

# CuRobo
- Apparently only works on Linux
- Tommy says won't work on WSL2 because
```
7 June 2024
[12:30] Tommy Wu (External)
you can enable gpu in wsl2 , but you can not run isaac sim in wsl2 now
[12:30] Tommy Wu (External)
since it need extra vulkan enabled which is not suppored by wsl GPU enbaled.
[12:31] Tommy Wu (External)
I have tried hard to enable that.
```
(clean WSL2 install on Ubunut 22)
(forgot to check python version)
(installed some apt repo source)
sudo apt install git
sudo apt install git-lfs
git clone https://github.com/NVlabs/curobo.git
pip install -e . --no-build-isolation
(Failed with message (no module torch))
sudo pip install torch
(Failed with no CUDA_HOME_ENVIRIONMENT)
(checked python was 3.10.12)
https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl
Read some of the above and installed the following
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0
wget https://developer.download.nvidia.com/compute/cuda/12.5.0/local_installers/cuda_12.5.0_555.42.02_linux.run
sudo sh cuda_12.5.0_555.42.02_linux.run
then ran:
pip install torch
python3
```
mike@Fearow:~$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.cuda.is_available()
True
>>> torch.cuda.device_count()
1
>>> quit()
```

pip install -e . --no-build-isolation
(took 10-20 minutes)
pip install pytest
python3 -m pytest .

"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64
set SETUPTOOLS_ENABLE_FEATURES="legacy-editable"
set DISTUTILS_USE_SDK=1


in `setup.py`
```
extra_cuda_args = {
    "nvcc": [
        "--threads=8",
        "-O3",
        "--ftz=true",
        "--fmad=true",
        "--prec-div=false",
        "--prec-sqrt=false",
        "--allow-unsupported-compiler",
    ]
}
```

Diffs:
diff D:/ov/curobo/src/curobo/curobolib/cpp/self_collision_kernel.cu D:/ov/curobo_for_windows/src/curobo/curobolib/cpp/self_collision_kernel.cu

Visual C++ is for some reason refusing to understand tagged initializers
Fixes :
line 134:
      // dist_t max_d = { .d = 0.0, .i = 0, .j = 0 };
      dist_t max_d = {0.0, 0, 0};

line 357:
      // dist_t  max_d[NBPB] = {{ .d = 0.0, .i = 0, .j = 0 } };
      dist_t  max_d[NBPB] = {{0.0,0,0 }};

in d:/ov/curobot/src/curobo/util/usd_helper.py
and changed 13 calls of `join_path` to `join_usd_path`
Note that there are also legitimate `join_path` calls that join file paths in this file
added at line 419:
```
def join_usd_path(root: str, sub_root: str):
    if root == "":
        return sub_root
    if sub_root == "":
        return root
    if root[-1] == "/":
        root = root[:-1]
    if sub_root[0] == "/":
        sub_root = sub_root[1:]
    newpath = root + "/" + sub_root
    return newpath
```

Start Isaac Sim
Open in Termaina Button
python d:/ov/curobo/examples/isaac_sim/motion_gen_reacher.py --robot franka.yml

Robot configs in:
`cd  ov\curboto\src\curobo\content\configs\robot`
Robot spheres in:

# Curobo on Ubuntu
- 26 July 2024
## Ubunutu
- Installed new Ubuntu 24.04 (Luxray) - bare bones (no office)

## OV
- Installed OV  `omnivers-launcher-liux.AppImage`
- Started by clicking on it from Desktop - command line launch didn't work
- Got stuck in Login Loop that only resolved when I switched to Microsfot Edge for Linux
- Installed Isaac Sim 2023.1.1 and tested with palletizing example

## curobo
- Grabbed curobo from curobo.org followed install instructions for installation with isaac sim
    - https://curobo.org/get_started/1_install_instructions.html
- Installed `ninja-build` and g++ (using `update-alternatives` package for gcc) - did not work with ver 13, did work with ver 11
    - https://linuxconfig.org/how-to-switch-between-multiple-gcc-and-g-compiler-versions-on-ubuntu-20-04-lts-focal-fossa
        -`$ sudo apt install build-essential`
        -`$ sudo apt -y install gcc-7 g++-7 gcc-8 g++-8 gcc-9 g++-9`
        -
        -`$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 7`
        -`$ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 7`
        -`$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8`
        -`$ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8`
        -`$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9`
        -`$ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 9`
        -
        -`$ sudo update-alternatives --config g++`
        -
        -`$ gcc --version`
        -`$ g++ --version`


# Steps for windows
- cloned curobo into `d:\ov\curobo2310`
- opened Visual Studio 2022 dev console
- changed env to x64
   - `"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64`
   - changed directory to `C:\Users\mwise\AppData\Local\ov\pkg\isaac-sim-2023.1.0-hotfix.1>`
- added `--allow-unsupproted-compiler` arg to `extra_cuda_args` in `setup.py`
- changed working dir to `d:\ov\curboto2310`
- `c:python -m pip install tomli wheel ninja`
- `c:python -m pip install -e .[isaacsim] --no-build-isolation`
```
D:\ov\curobo2310>diff D:\ov\curobo2310\src\curobo\curobolib\cpp\self_collision_kernel.cu  D:\ov\curobo400\src\curobo\curobolib\cpp\self_collision_kernel.cu
134c134,135
<       dist_t max_d = { .d = 0.0, .i = 0, .j = 0 };
---
>       // dist_t max_d = { .d = 0.0, .i = 0, .j = 0 };
>       dist_t max_d = {0.0, 0, 0};
357c358,359
<       dist_t  max_d[NBPB] = {{ .d = 0.0, .i = 0, .j = 0 } };
---
>       // dist_t  max_d[NBPB] = {{ .d = 0.0, .i = 0, .j = 0 } };
>       dist_t  max_d[NBPB] = {{0.0,0,0 }};

```
- `copy D:\ov\curobo400\src\curobo\curobolib\cpp\self_collision_kernel.cu  D:\ov\curobo2310\src\curobo\curobolib\cpp\self_collision_kernel.cu`
- compiled
- `c:python -m pytest .`
- Will have a couple of test failure starting at 68%
```
D:\ov\curobo2310>diff d:/ov/curobo400/src/curobo/util/usd_helper.py d:/ov/curobo2310/src/curobo/util/usd_helper.py
419,431d418
< def join_usd_path(root: str, sub_root: str):
<     if root == "":
<         return sub_root
<     if sub_root == "":
<         return root
<     if root[-1] == "/":
<         root = root[:-1]
<     if sub_root[0] == "/":
<         sub_root = sub_root[1:]
<     newpath = root + "/" + sub_root
<     return newpath
<
<
462d448
<
464,467c450
<         # print(f"add_subroot root:{root} sub_root:{sub_root}")
<         # joinp = join_usd_path(root, sub_root)
<         # print(f"add_subroot joinp:{joinp}")
<         xform = self.stage.DefinePrim(join_usd_path(root, sub_root), "Xform")
---
>         xform = self.stage.DefinePrim(join_path(root, sub_root), "Xform")
555c538
<         full_path = join_usd_path(base_frame, obstacles_frame)
---
>         full_path = join_path(base_frame, obstacles_frame)
583c566
<         root_path = join_usd_path(base_frame, obstacle.name)
---
>         root_path = join_path(base_frame, obstacle.name)
604c587
<         root_path = join_usd_path(base_frame, obstacle.name)
---
>         root_path = join_path(base_frame, obstacle.name)
627c610
<         root_path = join_usd_path(base_frame, obstacle.name)
---
>         root_path = join_path(base_frame, obstacle.name)
649c632
<         root_path = join_usd_path(base_frame, obstacle.name)
---
>         root_path = join_path(base_frame, obstacle.name)
729c712
<                 obs_name = join_usd_path(join_usd_path(base_frame, obstacles_frame), obs.name)
---
>                 obs_name = join_path(join_path(base_frame, obstacles_frame), obs.name)
798c781
<         mat_path = join_usd_path(object_path, material_name)
---
>         mat_path = join_path(object_path, material_name)
800c783
<         pbrShader = UsdShade.Shader.Define(self.stage, join_usd_path(mat_path, "PbrShader"))
---
>         pbrShader = UsdShade.Shader.Define(self.stage, join_path(mat_path, "PbrShader"))
871c854
<         robot_base_frame = join_usd_path(base_frame, robot_base_frame)
---
>         robot_base_frame = join_path(base_frame, robot_base_frame)
977c960
<         robot_base_frame = join_usd_path(base_frame, robot_base_frame)
---
>         robot_base_frame = join_path(base_frame, robot_base_frame)

D:\ov\curobo2310>
```
-`copy D:\ov\curobo400\src\curobo\curobolib\cpp\self_collision_kernel.cu  D:\ov\curobo2310\src\curobo\curobolib\cpp\self_collision_kernel.cu`
tests now run with two warnings (the "s" on the 90% line below)
```
D:\ov\curobo2310>c:python -m pytest .
================================================= test session starts =================================================
platform win32 -- Python 3.10.13, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\ov\curobo2310
configfile: pyproject.toml
plugins: anyio-4.4.0, torchtyping-0.1.4, typeguard-4.3.0
collected 249 items / 3 skipped

tests\cost_test.py .                                                                                             [  0%]
tests\cuda_robot_generator_test.py ....                                                                          [  2%]
tests\curobo_robot_world_model_test.py ...........                                                               [  6%]
tests\curobo_version_test.py .                                                                                   [  6%]
tests\geom_test.py ......                                                                                        [  9%]
tests\geom_types_test.py ......                                                                                  [ 11%]
tests\goal_test.py ..                                                                                            [ 12%]
tests\ik_config_test.py ....                                                                                     [ 14%]
tests\ik_module_test.py ......                                                                                   [ 16%]
tests\ik_test.py .....                                                                                           [ 18%]
tests\interpolation_test.py .                                                                                    [ 18%]
tests\kinematics_test.py ......                                                                                  [ 21%]
tests\mimic_joint_test.py ..                                                                                     [ 22%]
tests\motion_gen_api_test.py ...                                                                                 [ 23%]
tests\motion_gen_constrained_test.py ............................                                                [ 34%]
tests\motion_gen_cuda_graph_test.py .............                                                                [ 39%]
tests\motion_gen_eval_test.py ......                                                                             [ 42%]
tests\motion_gen_goalset_test.py ..                                                                              [ 42%]
tests\motion_gen_js_test.py ......                                                                               [ 45%]
tests\motion_gen_module_test.py ...................                                                              [ 53%]
tests\motion_gen_speed_test.py .........................                                                         [ 63%]
tests\motion_gen_test.py ...                                                                                     [ 64%]
tests\mpc_test.py ....                                                                                           [ 65%]
tests\multi_pose_test.py ......                                                                                  [ 68%]
tests\pose_reaching_test.py ..                                                                                   [ 69%]
tests\pose_test.py ..                                                                                            [ 69%]
tests\robot_assets_test.py ...............                                                                       [ 75%]
tests\robot_config_test.py ...                                                                                   [ 77%]
tests\robot_world_model_test.py ............                                                                     [ 81%]
tests\self_collision_test.py .....                                                                               [ 83%]
tests\trajopt_config_test.py ....                                                                                [ 85%]
tests\trajopt_test.py ..........                                                                                 [ 89%]
tests\usd_export_test.py s.                                                                                      [ 90%]
tests\voxel_collision_test.py .........                                                                          [ 93%]
tests\voxelization_test.py ..........                                                                            [ 97%]
tests\warp_mesh_test.py ...                                                                                      [ 99%]
tests\world_config_test.py ..                                                                                    [100%]

================================================== warnings summary ===================================================
tests/pose_test.py::test_pose_transform_point_grad
  C:\Users\mwise\AppData\Roaming\Python\Python310\site-packages\torch\autograd\gradcheck.py:915: UserWarning: Input #0 requires gradient and is not a double precision floating point or complex. This check will likely fail if all the inputs are not of double precision floating point or complex.
    warnings.warn(

tests/pose_test.py::test_pose_transform_point_grad
  C:\Users\mwise\AppData\Roaming\Python\Python310\site-packages\torch\autograd\gradcheck.py:915: UserWarning: Input #1 requires gradient and is not a double precision floating point or complex. This check will likely fail if all the inputs are not of double precision floating point or complex.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================== 248 passed, 4 skipped, 2 warnings in 441.04s (0:07:21) ================================

D:\ov\curobo2310>
```

On Luxray (Ubunutu 24.04)
Coloring changes to yellow for warning at 70% - not 90%
```
mike@luxray:~$ omni_python -m pytest .
========================================================================= test session starts =========================================================================
platform linux -- Python 3.10.13, pytest-8.2.2, pluggy-1.5.0
rootdir: /home/mike
plugins: anyio-3.7.1
collected 247 items / 4 skipped

ov/curobo/tests/cost_test.py .                                                                                                                                  [  0%]
ov/curobo/tests/cuda_robot_generator_test.py ....                                                                                                               [  2%]
ov/curobo/tests/curobo_robot_world_model_test.py ...........                                                                                                    [  6%]
ov/curobo/tests/curobo_version_test.py .                                                                                                                        [  6%]
ov/curobo/tests/geom_test.py ......                                                                                                                             [  9%]
ov/curobo/tests/geom_types_test.py ......                                                                                                                       [ 11%]
ov/curobo/tests/goal_test.py ..                                                                                                                                 [ 12%]
ov/curobo/tests/ik_config_test.py ....                                                                                                                          [ 14%]
ov/curobo/tests/ik_module_test.py ......                                                                                                                        [ 16%]
ov/curobo/tests/ik_test.py .....                                                                                                                                [ 18%]
ov/curobo/tests/interpolation_test.py .                                                                                                                         [ 19%]
ov/curobo/tests/kinematics_test.py ......                                                                                                                       [ 21%]
ov/curobo/tests/mimic_joint_test.py ..                                                                                                                          [ 22%]
ov/curobo/tests/motion_gen_api_test.py ...                                                                                                                      [ 23%]
ov/curobo/tests/motion_gen_constrained_test.py ............................                                                                                     [ 34%]
ov/curobo/tests/motion_gen_cuda_graph_test.py .............                                                                                                     [ 40%]
ov/curobo/tests/motion_gen_eval_test.py ......                                                                                                                  [ 42%]
ov/curobo/tests/motion_gen_goalset_test.py ..                                                                                                                   [ 43%]
ov/curobo/tests/motion_gen_js_test.py ......                                                                                                                    [ 45%]
ov/curobo/tests/motion_gen_module_test.py ...................                                                                                                   [ 53%]
ov/curobo/tests/motion_gen_speed_test.py .........................                                                                                              [ 63%]
ov/curobo/tests/motion_gen_test.py ...                                                                                                                          [ 64%]
ov/curobo/tests/mpc_test.py ....                                                                                                                                [ 66%]
ov/curobo/tests/multi_pose_test.py ......                                                                                                                       [ 68%]
ov/curobo/tests/pose_reaching_test.py ..                                                                                                                        [ 69%]
ov/curobo/tests/pose_test.py ..                                                                                                                                 [ 70%]
ov/curobo/tests/robot_assets_test.py ...............                                                                                                            [ 76%]
ov/curobo/tests/robot_config_test.py ...                                                                                                                        [ 77%]
ov/curobo/tests/robot_world_model_test.py ............                                                                                                          [ 82%]
ov/curobo/tests/self_collision_test.py .....                                                                                                                    [ 84%]
ov/curobo/tests/trajopt_config_test.py ....                                                                                                                     [ 86%]
ov/curobo/tests/trajopt_test.py ..........                                                                                                                      [ 90%]
ov/curobo/tests/voxel_collision_test.py .........                                                                                                               [ 93%]
ov/curobo/tests/voxelization_test.py ..........                                                                                                                 [ 97%]
ov/curobo/tests/warp_mesh_test.py ...                                                                                                                           [ 99%]
ov/curobo/tests/world_config_test.py ..                                                                                                                         [100%]

========================================================================== warnings summary ===========================================================================
ov/curobo/tests/pose_test.py::test_pose_transform_point_grad
  /home/mike/.local/share/ov/pkg/isaac-sim-2023.1.1/extscache/omni.pip.torch-2_0_1-2.0.2+105.1.lx64/torch-2-0-1/torch/autograd/gradcheck.py:688: UserWarning: Input #0 requires gradient and is not a double precision floating point or complex. This check will likely fail if all the inputs are not of double precision floating point or complex.
    warnings.warn(

ov/curobo/tests/pose_test.py::test_pose_transform_point_grad
  /home/mike/.local/share/ov/pkg/isaac-sim-2023.1.1/extscache/omni.pip.torch-2_0_1-2.0.2+105.1.lx64/torch-2-0-1/torch/autograd/gradcheck.py:688: UserWarning: Input #1 requires gradient and is not a double precision floating point or complex. This check will likely fail if all the inputs are not of double precision floating point or complex.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================= 247 passed, 4 skipped, 2 warnings in 285.56s (0:04:45) ========================================================
mike@luxray:~$
```

Windows test
`d:`
`cd \ov\curobo2310\examples\issac-sim`
`c:python motion_gen_reacher.py --robot franka.yml`