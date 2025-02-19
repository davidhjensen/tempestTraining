# Train YOLOv8 Model on Tempest
MSU maintains [Tempest](https://www.montana.edu/uit/rci/tempest/), a High Performance Computing (HPC) cluster, that is the largest supercomputer in Montana. We can utilize it to dramatically decrease training times for our computer vision system. This repo provides the folder structure and file templates to utilize Tempest to train a Yolo model from a Roboflow dataset. The following guide outlines the process to gain access to and train models on Tempest.

# Access Tempest
## New User Request
Resources on the supercomputer are available to all instructors and researchers for free, with the option to gain more access. To use Tempest as a student, you must be added as a user. Fill out the form by clicking “New User Request” on the [home page](https://www.montana.edu/uit/rci/tempest/) with Dr. Brad Whitaker as the PI. A training video and follow-up meeting are also required with details provided after submitting the form.

## MSU VPN for Remote Access
To access Tempest off of MSU’s network, a VPN is required. Follow instructions [here](https://www.montana.edu/uit/computing/desktop/vpn/) to download and setup the VPN.

## Environment Setup
Once you have been added as a user, we need to create an environment with the necessary packages to train our models with. Log in to [Tempest On-Demand](https://tempest-web.msu.montana.edu/pun/sys/dashboard), open a terminal, and execute the following commands:
```
cd $HOME
module load Anaconda3/2024.02-1
conda create -n YOLOv8 python=3.9
source activate YOLOv8
pip install ultralytics
pip3 install --upgrade torch torchvision torchaudio
pip install roboflow
```

# Clone Git Repo
Besides the scripts and data necessary to train models on any platform, Tempest uses a platform called SLURM to manage the cluster and schedule jobs. In order to run our scripts on the hardware we want, an additional .sbatch script is required. Clone this repository, which has the necessary folder structure and files for training models, into your home directory on Tempest.

# Train Model
## Data!
Use [Roboflow](https://roboflow.com/) to create a dataset, generate a version, and export the code snippet used to trian the model. Check out the README.md in the `/Data` folder to download the data, then come back here!
## Train
In `/Code`, open `train.py` and update the `MODEL_PATH`, `DATASET`, and `SAVE_TO` paths. Then, in `/Sbatch/train.sbatch`, update `<job_name>` and the path to the `train.py` script as needed. Finally, run `sbatch train.sbatch` in the Tempest terminal while in the `/Sbatch` folder to submit the job. To check on the progress, run `sacct`. Two files (`*.out` and `*.err`) will be generated. Check these for terminal outputs from the process (print statements, etc). The training results will be saved in the folder set by the `SAVE_TO` variable in `/Code/train.py`.