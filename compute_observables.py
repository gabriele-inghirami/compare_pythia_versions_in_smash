# Gabriele Inghirami - g.inghirami@gsi.de - 2023 - License: GPLv.3

# Units: if not specified differently, we use
# GeV for energy, mass and momenta
# fm for time and positions
# c units for the velocities

import math
import numpy as np
import os
import sys

# we consider an eta interval between -maxy-dy/2 and +maxy+dy/2,
# considered as external borders of the bins
# the center of the first cell is at -maxy, the center of the last cell at +maxy
maxy = 4.
dy = 0.2

# we consider a pT interval between 0 and maxpt+dpt/2
# the center of the first cell is at dpt/2, the center of the last cell is at maxpt
maxpt = 4.
dpt = 0.1

ny = int(2*maxy/dy+1)
npt = int(maxpt/dpt)
y_arr = np.linspace(-maxy,maxy,num=ny)
pt_arr = np.linspace(dpt/2,maxpt,num=npt)
top_abs_rapidity = y[-1] + dy/2
top_pt = maxpt + dpt/2

dNdy_buffer = np.zeros(ny,dtype=np.float64)
dNdy = np.zeros(ny,dtype=np.float64)
v1y_buffer = np.zeros(ny,dtype=np.float64)
v1y = np.zeros(ny,dtype=np.float64)
dNdpt_buffer = np.zeros(npt,dtype=np.float64)
dNdpt= np.zeros(npt,dtype=np.float64)
v2pt_buffer = np.zeros(npt,dtype=np.float64)
v2pt= np.zeros(npt,dtype=np.float64)

events = 0
tot_events = 0

if(len(sys.argv)<3):
   print('Syntax: ./compute_observables.py <output file label> <input file 1> [input file 2] ... [input file n]\n')
   sys.exit(2)

outfile_label = sys.argv[1]
infiles = sys.argv[2:]

for f in infiles:
    print("Opening "+f)
    with open(f,"r") as datei:
        events = 0
        try:
            for i in range(3):
                datei.readline() #we skip the first 3 lines
        except:
            continue
        while(True):
            try:
                n_items = int(datei.readline().split()[4])
            except:
                break
            try:
                dNdeta_buffer[:]=0
                for i in range(n_items):
                    stuff = datei.readline().split()
                    if (stuff[11] != "0"): 
                        En, px, py, pz = np.float64(stuff[5:9])
                        pt = math.sqrt( px**2 + py**2 )
                        if ((pt > top_pt) or (pt == 0) or (En < pz)):
                            continue
                        y = 0.5 * math.log( ( En + pz ) / ( En - pz ) )
                        if abs(y) >= top_abs_rapidity:
                            continue

                        # index for the rapidity array
                        h = int(math.floor((y + top_abs_rapidity)/dy)) # it's (y - (-top_abs_rapidity))/dy
                        # index for the transverse momentum array
                        k = int(math.floor(pt/dpt))

                        v1y_buffer[h] += px/pt
                        v2pt_buffer[k] += (px**2 - py**2)/(pt**2) 
                        dNdy_buffer[h] += 1
                        dNdpt_buffer[k] += 1

                if (i == n_items-1):
                    check_event = int(datei.readline().split()[2])
                    if events != check_event:
                        print("Event number mismatching in "+f+". Expected: "+str(events)+", found: "+str(check_event))
                        break
                    events += 1
                    v1y += v1y_buffer
                    v2pt += v2pt_buffer
                    dNdy += dNdy_buffer
                    dNdpt += dNdpt_buffer
            except:
                break
        tot_events += events

# output
sp = "    "
coord_format = "{:5.2f}"
data_format = "{:14.12g}"

fileout = open(outfile_label + "_v1_and_dN_vs_y.dat","w")
fileout.write("# events: " + str(tot_events) + "\n")
fileout.write("# pt range: " + str(pt[0]) + " - " + str(pt[-1]) + "\n")
fileout.write("# dy: " + str(dy) + "\n")
fileout.write("# y      dN/dy      v1\n")
for i in range(y_arr):
    if (dNdy[i] != 0):
        v1_value = data_format.format(v1y[i]/dNdy[i])
    else:
        v1_value = "0."
    fileout.write(coord_format.format(y_arr[i]) + sp + data_format.format(dNdy[i]/(tot_events*dy)) + sp + v1_value + "\n")
fileout.close()

fileout = open(outfile_label + "_v2_and_dN_vs_pt.dat","w")
fileout.write("# events: " + str(tot_events) + "\n")
fileout.write("# y range: " + str(y[0]) + " - " + str(y[-1]) + "\n")
fileout.write("# dpt: " + str(dpt) + "\n")
fileout.write("# pt      dN/dpt      v2\n")
for i in range(y_arr):
    if (dNdpt[i] != 0):
        v2_value = data_format.format(v2pt[i]/dNdpt[i])
    else:
        v2_value = "0."
    fileout.write(coord_format.format(pt_arr[i]) + sp + data_format.format(dNdpt[i]/(tot_events*dpt)) + sp + v2_value + "\n")
fileout.close()