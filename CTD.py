#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import os
import re 

def find_files():
    subname = "_ctm_fil_le_der_avg\.cnv"
    filenames = []
    files = os.listdir("Data")
    for file in files:
        filename = re.search(f"station\d?\d{subname}", file)
        if filename != None:
            filenames.append(filename.group(0))
    for filename in filenames:
        header_explanation = read_in(filename)

    print("Available Colnames:", header_explanation)
    coln = input("Choose Colname:")
    colnames = []
    for col in data.columns:
        colname = re.search(f'{coln}_\d?\d', col)
        if colname != None:
            colnames.append(colname.group(0))
    print(colnames)
    data.to_csv("CTD-Data.tsv", sep="\t")
    plots(data, coln, header_explanation)

def read_in(filename):
    data_headers = ["scan","prDM","t090C","c0S_per_m","sbeox0V","sbeox1V","flECO_AFL","upoly0","depSM","sal00","sbeox0ML_per_L","sbeox1ML_per_L","flag"]
    header_explanation = {"scan":"Scan Count", "prDM":"Pressure [db]", "t090C":"Temperature [$^\circ$C]", "c0S_per_m":"Conductivity [S/m]" ,"sbeox0V":"Oxygen [V]", "sbeox1V":"Oxygen [V]", "flECO_AFL":"Fluorescence [mg/m$^3$]", "upoly0":"Turbidity", "depSM": "Depth [salt water, m]", "sal00":"Salinity [PSU]", "sbeox0ML_per_L":"Oxygen [ml/l]", "sbeox1ML_per_L":"Oxygen [ml/l]","flag":"flag"}
    
    station = re.search('\d?\d', filename).group(0)
    global data
    try:
        data_headers_new = [f"{name}_{station}" for name in data_headers]
        df = pd.read_csv(f"Data/{filename}", sep=" ", skiprows=277, skipinitialspace=True, skip_blank_lines=True, names = data_headers_new)
        data = data.join(df, rsuffix="")
    except NameError:
        data_headers_first = [f"{name}_{station}" for name in data_headers]
        data = pd.read_csv(f"Data/{filename}", sep=" ", skiprows=277, skipinitialspace=True, skip_blank_lines=True, names = data_headers_first)
    return(header_explanation)

def plots(data, coln, header_explanation):
    cmap_colour = input("cmap colour:")
    fig, ax =plt.subplots(figsize=(8,4))

    cvalues = np.array([data[f"{coln}_1"],data[f"{coln}_10"],data[f"{coln}_2"],data[f"{coln}_9"],data[f"{coln}_3"],data[f"{coln}_8"],data[f"{coln}_4"],data[f"{coln}_5"],data[f"{coln}_7"],data[f"{coln}_6"]])
    depths = data.depSM_10
    stations = np.arange(1,10.5)

    PC = ax.pcolormesh(stations, depths, cvalues.T, cmap=cmap_colour, shading='auto')
    cbar = plt.colorbar(PC)

    cbar.set_label(header_explanation[coln])
    ax.set_xlabel("Station")
    ax.set_ylabel("Depth [m]")
    ax.invert_xaxis()
    depthsPlus1 = [14,40.2,46.5,43.5,17.3,13.5,15.4,25.9,31.1,38.3]
    ax.plot(stations, depthsPlus1, "k-")
    ax.set_xlim(1,10)
    ax.annotate("Byfjorden",xy = (2.5,1))
    ax.annotate("Havstensfjorden",xy = (7.5,1))
    ax.spines['top'].set_visible(False)
    plt.xticks([1,2,3,4,5,6,7,8,9,10],["S1","S10","S2","S9","S3","S8","S4","S5","S7","S6"])
    ax.set_ylim(np.max(depthsPlus1),0)
    ax.fill_between(stations, np.full(len(stations), np.max(depthsPlus1)), depthsPlus1, color="grey", alpha=1)
    ax.set_yticks([0,5,10,15,20,25,30,35,40])
    ax.set_yticks(np.arange(2,40), minor=True)
    # plt.grid()
    ax.yaxis.set_ticks_position('both')
    ax.tick_params(labeltop=False, labelright=True)
    # ax.grid(which="minor", linestyle="--", linewidth=0.5)
    savename = input("filename:")
    if savename != "":
        plt.savefig(f"./Images/{savename}.png", dpi=300 ,bbox_inches="tight")
    plt.show()
    

if __name__ == "__main__":
    plots(data)
