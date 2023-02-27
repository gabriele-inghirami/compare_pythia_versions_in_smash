#!/usr/bin/bash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-4:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=inghirami@fias.uni-frankfurt.de

Ecm=$1
pythia=$2
container=$3
sources=$4
job_seq_id=$5

wdir=$LH/test_pythia8309/run_$Ecm\_$pythia\_$job_seq_id
cfile=$LH/test_pythia8309/config_$Ecm.yaml

mkdir -p $wdir

# we compile smash before using it,
# so to use cpu spcific optimization flags without worries

cd $wdir
singularity exec $container cmake $sources
singularity exec $container make smash -j $SLURM_NTASKS

sleep 1

for i in $(seq 1 $SLURM_NTASKS)
do
    singularity exec $container ./smash -i $cfile -o out_$i &> log_$i &
done
wait
# this delay is just to prevent issues with the I/O buffering system
sleep 20
