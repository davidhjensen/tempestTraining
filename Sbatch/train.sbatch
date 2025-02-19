#!/bin/bash

## priority-bradwhitaker or group-bradwhitaker
## priority faster for gpupriority (2 A100 or 2 A40); H100 nextgen-gpu (4 H100 and 3 nodes) faster, but wait longer
#SBATCH --account=group-bradwhitaker

#SBATCH --partition=nextgen-gpu

#SBATCH --ntasks 1

#SBATCH --cpus-per-task 2

#SBATCH --gpus-per-task h100:4

## 1000G max for H100
## 500GB for Quad A100
#SBATCH --mem=256G

#SBATCH --time=0-04:00:00

#SBATCH --job-name=<job_name>

## %x is the job name and %j and the job number
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err

module load Anaconda3/4.0.0

source activate $HOME/.conda/envs/YOLOv8

python $HOME/tempestTraining/Code/train.py