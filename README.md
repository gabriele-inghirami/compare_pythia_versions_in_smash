## Introduction:

This repository contains the scripts and the config file used to compare the results of SMASH compiled with Pythia version 8.307 and 8.309.
This material, with minor modifications, should be reusable also for future Pythia version.
The slurm scripts have been written for the Virgo cluster at GSI, but they can be easily adapted for other clusters.
Tested with Python version: 3.8.10 and gnuplot version: 5.4.2.
Usage date: 26/02/2023.

## How to use the content of this repository

Here is a possible sequence of steps, which can be modified accoding to specific needs/situations/enviroments/tastes:
- clone the **SMASH** repository (in general, the private development version)
- create a branch to use Pythia 8.309. It can be convenient to use a worktree, so to check two branches at the same time. For example, `git worktree add ../smash-devel-py309 $USER/test_pythia8309` creates the branch _$USER/test_pythia8309_ in the directory _../smash-devel-py309_. As an alternative, one can just copy the sources into another directory or compile and save the executables after checking each branch.
- in the branch to be compiled with the new Pythia version one needs to change at least _src/CMakeLists.txt_ and _cmake/FindSMASH.cmake_ and update the Pythia version number (these changes are required just to tell _cmake_ which version to use, then, of course, many other changes in the code might be needed to make it working and, even if not, the documentation and the Dockerfiles must also be updated).
- clone this repository and enter inside its main directory
- these scripts assume to be launched from the main directory of the repository, that the _../smash-devel_ directory contains the **SMASH** sources requiring the older (8.307) Pythia version and the _../smash-devel-py309_ the newer one (8.309)
- launch the **SMASH** runs with `./launch_runs_smash.bash` (which in turns launches several times the slurm script _run_smash.slurm_, using _config_200.yaml_ as configuration file)
- launch the slurm script for the postprocessing with `sbatch postproc_smash.slurm`, which executes many instances of the script _compute_observables.py_
- combine the results with something like `python3 combine_results.py results_8.307 *8.307*.pickle` (separately for each Pythia version). The merging uses only _.pickle_ archive files.
- make the plots with `gnuplot make_plots.gp`. The gnuplot script uses only the _.txt_ files which are produced by _combine_results.py_ or by _compute_obervables.py_ when their internal harcoded option _print_ascii_ is set to _True_. It is often convenient and easier to make the plots locally after copying the final output _.txt_ files. from the cluster.
- it is possible to convert the plots from _.eps_ to _.pdf_ format with: `for i in *.eps; do ps2pdf -dEPSCrop $i; done` (but there are of course several other ways/programs)
