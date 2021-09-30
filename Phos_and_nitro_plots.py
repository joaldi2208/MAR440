#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_data = pd.read_csv("data0.tsv", sep="\t")
p_data = pd.read_csv("data1.tsv", sep="\t")
ctd_data = pd.read_csv("ctd_data_day2/CTD-Data.tsv", sep="\t")

# print(ctd_data.depSM_6)
station_depths = np.array([13,10,5,1,45.5,35,23.1,15,10,5.2,1,16.3,10,5,1,14.4,10,5,1,24.9,15,10,5,1,37.3,25,14.5,10,5,1])
orginal_stations = {"depSM_1":[1,5,10,13],"depSM_2":[1,5,10,15,23,35,45],"depSM_3":[1,5,10,16],"depSM_4":[1,5,10,14],"depSM_5":[1,5,10,15,25],"depSM_6":[1,5,15,25,37]}
# fake stations
stations = {"depSM_1":[1,5,10,13],"depSM_2":[1,5,10,15,23,35,43],"depSM_3":[1,5,10,16],"depSM_4":[1,5,10,14],"depSM_5":[1,5,10,15,25],"depSM_6":[1,5,15,25,36]}

# station_depths_unique = np.unique(station_depths)
# print(station_depths_unique)
#for i in range(1,11):
#    print(ctd_data[f"depSM_{i}"])

counter = 1
for key, value in stations.items():
    depths = ctd_data.loc[ctd_data[key].isin(value)]
    # print(depths)
    depths = depths.reset_index()
    n_data[key] = depths[key]
    n_data[f"Fluoro_{counter}"] = depths[f"flECO_AFL_{counter}"]    
    p_data[key] = depths[key]
    p_data[f"Fluoro_{counter}"] = depths[f"flECO_AFL_{counter}"]    
    counter += 1

# print(n_data.Conc, n_data.SampleID)
n_data.to_csv("n_data_w_F_D.tsv", sep="\t")

# print(n_data.SampleID)


def plots(data, ind, ind_c):
    for i in range(1,7):
        # plt.scatter(data.Conc[ind_c[i-1][0]:ind_c[i-1][1]], data[f"Fluoro_{i}"][0:ind[i-1]].values, s = data[f"depSM_{i}"][0:ind[i-1]].values*10, label=f"S{i}")
        # print(data.Conc[ind_c[i-1][0]:ind_c[i-1][1]][::-1])
        ax.scatter(data[f"Fluoro_{i}"][0:ind[i-1]].values, data[f"depSM_{i}"][0:ind[i-1]].values, s = data.Conc[ind_c[i-1][0]:ind_c[i-1][1]][::-1]*25, label=f"S{i}")        
        # print(data.SampleID[ind_c[i-1][0]:ind_c[i-1][1]])
        
ind = [4,5,3,4,4,4]
ind_c = [[0,4],[4,9],[11,14],[15,19],[19,23],[24,28]]
datas = [n_data, p_data]
counter2 = 0
for data in datas:
    fig, ax = plt.subplots()
    plots(data, ind, ind_c)
    plt.legend()
    ax.invert_yaxis()
    plt.ylabel("Depth [m]")
    plt.xlabel("Fluorescence [mg/m$^3$]")
    if counter2 == 0:
        plt.title("Nitrate")
        plt.savefig("./ctd_data_day2/Images/Nitrate.png", dpi=300, bbox_inches="tight")
    elif counter2 == 1:
        plt.title("Phosphate")
        plt.savefig("./ctd_data_day2/Images/Phospate.png", dpi=300, bbox_inches="tight")
    plt.show()
    counter2 += 1

# plt.scatter(n_data.Conc[0:4], n_data.Fluoro_1[0:4], s = n_data.depSM_1[0:4]*10, label="S1")
# plt.scatter(n_data.Conc[4:9], n_data.Fluoro_2[0:5], s = n_data.depSM_2[0:5]*10, label="S2")
# plt.scatter(n_data.Conc[12:15], n_data.Fluoro_3[0:3], s = n_data.depSM_2[0:3]*10, label="S3")
# plt.scatter(n_data.Conc[16:20], n_data.Fluoro_4[0:4], s = n_data.depSM_2[0:4]*10, label="S4")
# plt.scatter(n_data.Conc[20:24], n_data.Fluoro_5[0:4], s = n_data.depSM_2[0:4]*10, label="S5")
# plt.scatter(n_data.Conc[25:28], n_data.Fluoro_6[0:3], s = n_data.depSM_2[0:3]*10, label="S6")
# plt.xlabel("Conc [$\mu$g/L]")
# plt.ylabel("Fluorescence [mg/m$^3$]")
# plt.legend()
# plt.show()
