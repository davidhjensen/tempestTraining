#!/bin/bash

#SBATCH --account=<whitaker's acct>

#SBATCH --partition=<gpu node on his acct?>

#SBATCH --cpus-per-task 2

#SBATCH --gpus-per-task a40:2

#SBATCH --mem=128G

#SBATCH --time=0-01:00:00

#SBATCH --job-name=train

#SBATCH --output=train-%j.out

#SBATCH --error=train-%j.err

module load Anaconda3/5.3.0

source activate $HOME/.conda/envs/robosub_yolov8

python $HOME/robosub/code/modelTuning.py
