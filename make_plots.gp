### Pythia versions *********

versA="8.307"
versB="8.309"

### Terminal type and line styles **********

set term pos eps col enh font "Helvetica, 22"
ending=".eps" # please, change it if you change terminal type

set style line 1 dt 1 lc "navy" lw 4
set style line 2 dt 3 lc "red" lw 4

set mxtics 4
set mytics 4

prefix="results_"

### Plot title (system, centrality, etc.) **********

set title "Au+Au, {/Symbol \326}s = 200 GeV, b = 6 fm, all hadrons"

### Plots vs rapidity **********

suffix="_v1_and_dN_vs_y.txt"

set xlabel "y (rapidity)"

fA=prefix.versA.suffix
fB=prefix.versB.suffix

### dNdy *********

set out "dNdy_SMASH_Pythia_".versA."_vs_".versB.ending
set ylabel "dN/dy"
plot fA u 1:2 w l ls 1 t versA, fB u 1:2 w l ls 2 t versB

### v1 **********

set out "v1_SMASH_Pythia_".versA."_vs_".versB.ending
set ylabel "v_1"
plot fA u 1:3 w l ls 1 t versA, fB u 1:3 w l ls 2 t versB

### Plots vs tranverse momentum pt **********

suffix="_v2_and_dN_vs_pt.txt"

set xlabel "p_T [GeV]"

fA=prefix.versA.suffix
fB=prefix.versB.suffix

### dNdpt *********

set mxtics 5

set out "dNdpt_SMASH_Pythia_".versA."_vs_".versB.ending
set ylabel "dN/dp_T [GeV^{-1}]"
plot fA u 1:2 w l ls 1 t versA, fB u 1:2 w l ls 2 t versB

set out "dNdpt_SMASH_Pythia_".versA."_vs_".versB."_logscale".ending
set logscale y
set format y "10^{%L}"
plot fA u 1:2 w l ls 1 t versA, fB u 1:2 w l ls 2 t versB
unset logscale y
set format y

### v2 **********

set out "v2_SMASH_Pythia_".versA."_vs_".versB.ending
set ylabel "v_2"
set xrange [0:2.5]
set yrange [0:0.05]

plot fA u 1:3 w l ls 1 t versA, fB u 1:3 w l ls 2 t versB
