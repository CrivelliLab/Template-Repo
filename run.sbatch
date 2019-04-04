#!/bin/bash
#SBATCH --job-name="run_demo"
#SBATCH --output="run.out"
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH -t 00:30:00

# Load Modules
module load python/3.6-anaconda-4.4

# Variables
CORES = 64

python3 src/transform_data.py
