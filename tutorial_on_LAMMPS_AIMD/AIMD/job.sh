#!/bin/bash
#SBATCH -A standby
#SBATCH -N 4
#SBATCH -n 512
#SBATCH -t 4:00:00
#SBATCH --job-name ZIS-SAC


module load vasp/6.4.1


cd  $SLURM_SUBMIT_DIR
mpirun -np 512 vasp_std > outVASP
