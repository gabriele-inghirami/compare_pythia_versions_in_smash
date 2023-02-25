#!/usr/bin/bash
#SBATCH --job-name=postproc_smash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --ntasks=40
#SBATCH --mem-per-cpu=3G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-3:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=inghirami@fias.uni-frankfurt.de

container=$LH/smash_environment_for_dev_pythia_8309.sif

vers_old=8.307
vers_new=8.309

for i in {1..20}
do
singularity exec $container python3 compute_observables.py results_$vers_old\_$i series*/run_200_$vers_old\_$i/out_[1-10]/particle_lists.oscar &> log_$vers_old\_$i &
singularity exec $container python3 compute_observables.py results_$vers_new\_$i series*/run_200_$vers_new\_$i/out_[1-10]/particle_lists.oscar &> log_$vers_new\_$i &
done
wait
sleep 60
