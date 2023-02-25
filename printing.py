def print_data(print_ascii, outputfile_label, tot_events, pt_arr, y_arr, dNdpt, dNdy, v1y, v2pt, verbose):
    
    import pickle
    import os.path
    from datetime import datetime

    # if the pickle outputfile already exists, we rename the common output file label
    if (os.path.isfile(outputfile_label + ".pickle")):
        now = datetime.now()
        new_outputfile_label = outputfile_label + now.strftime("_%Y_%m_%d__%H_%M_%S")
        if verbose > 0:
            print("Warning: output file " + outputfile_label + "already exists")
            print("Please, check again to have used the correct command syntax")
            print("Anyway, the output file of this program will be changed into " + new_outputfile_label)
        outputfile_label = new_outputfile_label
        
    dpt = pt_arr[1] - pt_arr[0]
    dy =y_arr[1] - y_arr[0]
    if (print_ascii):
        sp = "    "
        coord_format = "{:5.2f}"
        data_format = "{:14.12g}"

        fileout = open(outputfile_label + "_v1_and_dN_vs_y.txt", "w")
        fileout.write("# events: " + str(tot_events) + "\n")
        fileout.write("# pt range: " + str(pt_arr[0]) + " - " + str(pt_arr[-1]) + "\n")
        fileout.write("# dy: " + str(dy) + "\n")
        fileout.write("# y      dN/dy      v1\n")
        for i in range(len(y_arr)):
            if (dNdy[i] != 0):
                v1_value = data_format.format(v1y[i]/dNdy[i])
            else:
                v1_value = "0."
            fileout.write(coord_format.format(y_arr[i]) + sp + data_format.format(dNdy[i]/(tot_events*dy)) + sp + v1_value + "\n")
        fileout.close()

        fileout = open(outputfile_label + "_v2_and_dN_vs_pt.txt", "w")
        fileout.write("# events: " + str(tot_events) + "\n")
        fileout.write("# y range: " + str(y_arr[0]) + " - " + str(y_arr[-1]) + "\n")
        fileout.write("# dpt: " + str(dpt) + "\n")
        fileout.write("# pt      dN/dpt      v2\n")
        for i in range(len(pt_arr)):
            if (dNdpt[i] != 0):
                v2_value = data_format.format(v2pt[i]/dNdpt[i])
            else:
                v2_value = "0."
            fileout.write(coord_format.format(pt_arr[i]) + sp + data_format.format(dNdpt[i]/(tot_events*dpt)) + sp + v2_value + "\n")
        fileout.close()

    with open(outputfile_label + ".pickle", "wb") as outf:
        pickle.dump((tot_events, pt_arr, y_arr, dNdpt, dNdy, v1y, v2pt), outf)