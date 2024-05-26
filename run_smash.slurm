#!/usr/bin/bash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=2G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-5:00:00
#SBATCH --mail-type=NONE
##SBATCH --mail-user=<your email here>

Ecm=$1
pythia=$2
container=$3
sources=$4
job_seq_id=$5

wdir=$LH/compare_pythia_versions_in_smash/RUNS/run_$Ecm\_$pythia\_$job_seq_id
bdir=/tmp/build_$Ecm\_$pythia\_$job_seq_id
cfile=$LH/compare_pythia_versions_in_smash/config_$Ecm.yaml

mkdir -p $wdir $bdir

# we compile smash before using it,
# so to use cpu spcific optimization flags without worries
# for the executable, we use the local /tmp directory

cd $bdir
singularity exec $container cmake $sources
singularity exec $container make smash -j $SLURM_NTASKS
rm -rf 3* Testing src CMake* doc Makefile DartConfiguration.tcl compile_commands.json *.cmake

sleep 1

cd $wdir
for i in $(seq 1 $SLURM_NTASKS)
do
    singularity exec $container $bdir/smash -i $cfile -o out_$i &> log_$i &
done
wait
# this delay is just to prevent issues with the I/O buffering system
rm -rf tabulations
sleep 10
