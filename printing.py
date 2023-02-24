def print_data(print_ascii, outfile_label, tot_events, pt_arr, y_arr, dNdpt, dNdy, v1y, v2pt):
    dpt = pt_arr[1] - pt_arr[0]
    dy =y_arr[1] - y_arr[0]
    if (print_ascii):
        sp = "    "
        coord_format = "{:5.2f}"
        data_format = "{:14.12g}"

        fileout = open(outfile_label + "_v1_and_dN_vs_y.txt", "w")
        fileout.write("# events: " + str(tot_events) + "\n")
        fileout.write("# pt range: " + str(pt[0]) + " - " + str(pt[-1]) + "\n")
        fileout.write("# dy: " + str(dy) + "\n")
        fileout.write("# y      dN/dy      v1\n")
        for i in range(y_arr):
            if (dNdy[i] != 0):
                v1_value = data_format.format(v1y[i]/dNdy[i])
            else:
                v1_value = "0."
        fileout.write(coord_format.format(
            y_arr[i]) + sp + data_format.format(dNdy[i]/(tot_events*dy)) + sp + v1_value + "\n")
        fileout.close()

        fileout = open(outfile_label + "_v2_and_dN_vs_pt.txt", "w")
        fileout.write("# events: " + str(tot_events) + "\n")
        fileout.write("# y range: " + str(y[0]) + " - " + str(y[-1]) + "\n")
        fileout.write("# dpt: " + str(dpt) + "\n")
        fileout.write("# pt      dN/dpt      v2\n")
        for i in range(y_arr):
            if (dNdpt[i] != 0):
                v2_value = data_format.format(v2pt[i]/dNdpt[i])
            else:
                v2_value = "0."
        fileout.write(coord_format.format(
            pt_arr[i]) + sp + data_format.format(dNdpt[i]/(tot_events*dpt)) + sp + v2_value + "\n")
        fileout.close()

    with open(outfile_label + ".pickle", "wb") as outf:
        pickle.dump((tot_events, pt_arr, y_arr, dNdpt, dNdy, v1y, v2pt), outf)
