#!/bin/bash

## priority-bradwhitaker or group-bradwhitaker
## priority faster for gpupriority (2 A100 or 2 A40); H100 nextgen-gpu (4 H100 and 3 nodes) faster, but wait longer
#SBATCH --account=priority-bradwhitaker

#SBATCH --partition=gpupriority

#SBATCH --cpus-per-task 2

#SBATCH --gpus-per-task a100:2

## 1000G max for H100
## 500GB for Quad A100
#SBATCH --mem=64G

#SBATCH --time=0-01:00:00

#SBATCH --job-name=train

## %x is the job name and %j and the job number
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err

module load Anaconda3/5.3.0

source activate $HOME/.conda/envs/robosub_yolov8

python $HOME/robosub/code/dualGPUTrain.py
