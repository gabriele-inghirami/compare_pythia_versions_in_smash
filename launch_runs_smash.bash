Ecm=200
pythia_old=8.309
pythia_new=8.310
sif_pythia_old=$LH/smash-3.0_max.sif
sif_pythia_new=$LH/smash-pythia8310.sif
source_old=/SMASH/smash
source_new=$source_old #we are taking the sources from different containers, so they have the same name, but they are different directories
for h in {1..30}
do
sbatch --job-name=smash_$Ecm\_$pythia_old\_$h run_smash.slurm $Ecm $pythia_old $sif_pythia_old $source_old $h
sbatch --job-name=smash_$Ecm\_$pythia_new\_$h run_smash.slurm $Ecm $pythia_new $sif_pythia_new $source_new $h
done
