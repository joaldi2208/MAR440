#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd


# read in data
n_data = pd.read_excel("NutrientDataG2.xlsx",sheet_name=1, header=3, names=["LRconc","LRabsorb","NANs","SampleID","Absorb"])

p_data = pd.read_excel("NutrientDataG2.xlsx",sheet_name=0 ,header=3, names=["LRconc","LRabsorb","NANs","SampleID","Absorb"])


def preProcessing(datas):
    ''' receives df and deletes NANs '''
    for ind, data in enumerate(datas):
        data = data.drop(["NANs"], axis=1)
        x = data.LRconc.array.dropna()
        y = data.LRabsorb.array.dropna()
        analyseNutrient(x,y,data,ind)


def analyseNutrient(x,y,data,ind):
    name = ["Nitrate", "Phosphate"]
    slope, intercept, r, p, se = stats.linregress(x, y)
    print(f"slope:{slope} \n intercept:{intercept} \n r:{r} \n p:{p} \n se:{se}")

    plt.plot(x, y,"k.", label="Standard Samples")
    plt.plot(np.arange(1,np.max(x)+2), slope * np.arange(1,max(x)+2) + intercept, "k-", label=f" Slope:{round(slope,5)} \n Intercept:{round(intercept,5)} \n R$^2$:{round(r**2,5)}")
    plt.xlabel("Concentration [$\mu$mol/L]")
    plt.ylabel("Absorbance")
    plt.legend()
    plt.savefig(f"LR_{name[ind]}")
    plt.show()

    data["Conc"] = (data.Absorb / slope) - intercept
    data.to_csv(f"data{ind}.tsv".format(ind), sep="\t")
    
    plt.plot(x,y,"k.", label="Standard Samples")
    plt.plot(data.Conc, data.Absorb,"r.", label="Samples")
    plt.plot(np.arange(1,np.max(x)+2), slope * np.arange(1,max(x)+2) + intercept, "k-", label=f" slope:{round(slope,5)} \n intercept:{round(intercept,5)} \n R$^2$:{round(r**2,5)}")
    plt.xlabel("Concentration [$\mu$mol/L]")
    plt.ylabel("Absorbance")
    plt.legend()
    plt.show()

preProcessing([n_data, p_data])

