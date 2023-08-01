#!/usr/bin/bash
#SBATCH --job-name=postproc_smash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --ntasks=60
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-0:15:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=inghirami@fias.uni-frankfurt.de

container=$LH/smash-pythia8310.sif
datadir=$LH/compare_pythia_versions_in_smash/RUNS/

vers_old=8.309
vers_new=8.310

for i in {1..30}
do
singularity exec $container python3 compute_observables.py $datadir/results_$vers_old\_$i.dat $datadir/run_200_$vers_old\_$i/out_{1..10}/particle_lists.oscar &> log_$vers_old\_$i &
singularity exec $container python3 compute_observables.py $datadir/results_$vers_new\_$i.dat $datadir/run_200_$vers_new\_$i/out_{1..10}/particle_lists.oscar &> log_$vers_new\_$i &
done
wait
sleep 60
