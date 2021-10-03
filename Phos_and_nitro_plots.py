#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

n_data = pd.read_csv("data0.tsv", sep="\t")
p_data = pd.read_csv("data1.tsv", sep="\t")
ctd_data = pd.read_csv("../ctd_data_day2/CTD-Data.tsv", sep="\t")


original_stations = {"depSM_1":[1,5,10,13],"depSM_2":[1,5,10,15,23,35,45],"depSM_3":[1,5,10,16],"depSM_4":[1,5,10,14],"depSM_5":[1,5,10,15,25],"depSM_6":[1,5,15,25,37]}

rows = [[0,4],[4,11],[11,15],[15,19],[19,24],[24,29]]

group_depth = ctd_data.groupby(pd.cut(ctd_data.depSM_2, np.arange(0,37,3))).mean()


for i in range(6):
    fig = plt.figure()
    ax = host_subplot(111, axes_class = AA.Axes, figure = fig)
    ax.plot(group_depth[f"flECO_AFL_{i+1}"], group_depth["Unnamed: 0"], "black", label="Fluorescence")
    ax.set_ylabel("Depth [m]")
    ax.set_xlabel("Fluorescence [mg/m$^3$]")
    ax.set_title(f"Station {i+1}")
    ax2 = ax.twiny()
    ax2.plot(n_data.Conc[rows[i][0]:rows[i][1]][::-1],original_stations[f"depSM_{i+1}"], "green", label="Nitrate")
    ax2.plot(p_data.Conc[rows[i][0]:rows[i][1]][::-1],original_stations[f"depSM_{i+1}"], "orange", label="Phosphate")
    ax2.set_xlabel("Concentration [mmol/L]")
    ax.invert_yaxis()
    plt.subplots_adjust(bottom = 0.2)
    offset = -40
    new_fixed_axis = ax2.get_grid_helper().new_fixed_axis
    ax2.axis['bottom'] = new_fixed_axis(loc = 'bottom',
                                    axes = ax2,
                                    offset = (0, offset))
    ax2.axis['bottom'].toggle(all = True)
    ax.legend(loc="upper right")
    plt.savefig(f"F_N_P_station{i+1}.png", dpi=300, bbox_inches="tight")
    plt.show()
