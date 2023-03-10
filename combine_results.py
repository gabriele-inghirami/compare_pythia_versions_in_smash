# Gabriele Inghirami - g.inghirami@gsi.de - 2023 - License: GPLv.3

# Units: if not specified differently, we use
# GeV for energy, mass and momenta
# fm for time and positions
# c units for the velocities

import math
import numpy as np
import pickle
import sys
import os.path

from printing import print_data # this is a local function

# tunes the verbosity level
# 0 = only errors messages
# 1 = errors and warning messages
# >=2 = progress status of the progra
verbose = 2

# decides whether to print also an ascii output or not
print_ascii = True

N_args=len(sys.argv)
N_input_files=N_args-2

if(N_input_files<1):
   print('Syntax: ./combine_results.py <outputfile label> <inputfile 1> <inputfile 2> ... [inputfile n]')
   print("(If only one inputfile is given, this script will just print the ascii output, if enabled.)")
   sys.exit(1)

outputfile_label = sys.argv[1]

with open(sys.argv[2],"rb") as infile:
    if verbose > 1:
        print("Opening: "+sys.argv[2])
    data = pickle.load(infile)
    tot_events, pt_arr, y_arr, dNdpt, dNdy, v1y, v2pt = data[:]
data=None

for fi in range(3,N_args):
    if verbose > 1:
        print("Opening: "+sys.argv[fi])
    try:
        with open(sys.argv[fi],"rb") as infile:
            data = pickle.load(infile)
    except:
        print("Error in reading "+sys.argv[fi])
        continue
    tot_events_new, pt_arr_new, y_arr_new, dNdpt_new, dNdy_new, v1y_new, v2pt_new = data[:]
    data = None
    if ((pt_arr_new.all() != pt_arr.all()) or (y_arr_new.all() != y_arr.all())):
        print("Warning, I skip input file "+sys.argv[fi])
        print("because the pt and y arrays are different")
        continue
    tot_events += tot_events_new
    dNdpt += dNdpt_new
    dNdy += dNdy_new
    v1y += v1y_new
    v2pt += v2pt_new

# output
print_data(print_ascii, outputfile_label, tot_events, pt_arr, y_arr, dNdpt, dNdy, v1y, v2pt, verbose)
