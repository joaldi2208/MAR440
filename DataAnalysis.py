#!/usr/bin/python3

import pandas as pd

from LR import preProcessing
from CTD import find_files
from PNF import read_in

                
n_data = pd.read_excel("./Data/NutrientDataG2.xlsx",sheet_name=1, header=3, names=["LRconc","LRabsorb","NANs","SampleID","Absorb"]) 
p_data = pd.read_excel("./Data/NutrientDataG2.xlsx",sheet_name=0 ,header=3, names=["LRconc","LRabsorb","NANs","SampleID","Absorb"]) 

def start():
    print("-------------------------------------------------------")
    print("\t \t \t Available Programs: \n ")                                                               
    print("0 \t -> \t Exit")                                                                         
    print("1 \t -> \t Linear Regression")                                                            
    print("2 \t -> \t CTD Data Analysis")                                                            
    print("3 \t -> \t Nitrate and Phosphate Concentration and Fluorescence against Depth \n")           
    choice = input("\t Which Programm should be started?:")                                       
    print("-------------------------------------------------------")
                                                                                            
    while choice != "0":
        if choice == "1":
           preProcessing([n_data, p_data]) 
        elif choice == "1?":
            def LR_explanation():
                '''Short explanation about the requirements for program 1 which calculates and plots a linear regression for the nitrate and phosphate samples'''
                print("+++++++++++++++++++++++++++++++++start help++++++++++++++++++++++++++++++++++")
                print("\n \t \t \t Linear Regression")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print("needed Data: \t 'NutrientDataG2.xlsx' in the same folder. \n")
                print("structure of 'NutrientDataG2.xlsx':")
                print("At least two sheets. First one is for phosphate, second one is for nitrate")
                print("Five columns: Concentration standards, Absorbtion standards, NaNs, SampleID, Sample Absorbtion \n")
                print("++++++++++++++++++++++++++++++++end help++++++++++++++++++++++++++++++++++++")
            LR_explanation()
        elif choice == "2":
           find_files()
        elif choice == "2?":
            def CTD_explanation():
                '''Short explanation about the requirements for program 2 which creates a DataFrame for all CTD Measurements and creates heatmaps of the measured properties on a hardcoded topography'''
                print("+++++++++++++++++++++++++++++++++start help++++++++++++++++++++++++++++++++++")
                print("\n \t \t \t CTD-Data Analysis")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print("needed Data: \t files that end with 'ctm_fil_le_der_avg.cnv' \n")
                print("++++++++++++++++++++++++++++++++end help++++++++++++++++++++++++++++++++++++")
            CTD_explanation()
        elif choice == "3":
            read_in()
        elif choice == "3?":
            def P_N_F_explanation():
                '''Short explanation about the requirements for program 2 which plots a figure with
     depth on the y-axis and the fluorescence and nitrate and phosphate concentration on the x-axis
     for all stations'''
                print("+++++++++++++++++++++++++++++++++start help++++++++++++++++++++++++++++++++++")
                print("\n \t \t \t Phosphate Nitrate Fluorescence Plots")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") 
                print("needed Data: \t 'data0.tsv', 'data1.tsv' (created by program 1) and 'CTD-Data.tsv' (created by program 2) in the same folder. \n")
                print("++++++++++++++++++++++++++++++++end help++++++++++++++++++++++++++++++++++++")
            P_N_F_explanation()
        else:
            print("Please enter on of the numbers below")

        print("-------------------------------------------------------")
        print("\t \t \t Available Programs: \n ")                                                               
        print("0 \t -> \t Exit")                                                                         
        print("1 \t -> \t Linear Regression")                                                            
        print("2 \t -> \t CTD Data Analysis")                                                            
        print("3 \t -> \t Nitrate and Phosphate Concentration and Fluorescence against Depth \n")           
        choice = input("\t Which Programm should be started?:")                                       
        print("-------------------------------------------------------")


if __name__ == "__main__":
    start()
