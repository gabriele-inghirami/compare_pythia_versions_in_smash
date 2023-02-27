Ecm=200
pythia_old=8.307
pythia_new=8.309
sif_pythia_old=$LH/smash_environment_for_dev-2022.12.17.sif
sif_pythia_new=$LH/smash_environment_for_dev_pythia_8309.sif
source_old=$LH/smash-devel
source_new=$LH/smash-devel-py309
for h in {1..20}
do
sbatch --job-name=smash_$Ecm\_$pythia_old\_$h run_smash.bash $Ecm $pythia_old $sif_pythia_old $source_old $h
sbatch --job-name=smash_$Ecm\_$pythia_new\_$h run_smash.bash $Ecm $pythia_new $sif_pythia_new $source_new $h
done
