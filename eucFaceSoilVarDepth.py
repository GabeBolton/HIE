# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:14:24 2018

@author: jbgab
"""
#  This 

import glob
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import SoilVarDepth

filePath='eucfacesoilsensorfiles\\'
outPath='eucfacesoilsensorFigures\\'
files = glob.glob(filePath+'*SoilVars*.dat')#uses regex to access a list of files
print(files)


#list columns that you want to plot
theta1=['Theta5_1_Avg', 'Theta30_1_Avg', 'ThetaHL_1_Avg','Theta75_1_Avg']
theta2=['Theta5_2_Avg', 'Theta30_2_Avg', 'ThetaHL_2_Avg','Theta75_2_Avg']
TDR=['TDRTemp_1_Avg', 'TDRTemp_2_Avg','TDRTemp_3_Avg', 'TDRTemp_4_Avg', 'TDRTemp_5_Avg', 'TDRTemp_6_Avg','TDRTemp_7_Avg', 'TDRTemp_8_Avg']
T=['T5cm_1_Avg', 'T10cm_1_Avg',  'T20cm_1_Avg',  'T30cm_1_Avg',  'T50cm_1_Avg', 'T100cm_1_Avg','T5cm_2_Avg','T10cm_2_Avg','T20cm_2_Avg','T30cm_2_Avg','T50cm_2_Avg','T100cm_2_Avg']
EC=['EC_1_Avg', 'EC_2_Avg', 'EC_3_Avg', 'EC_4_Avg', 'EC_5_Avg', 'EC_6_Avg','EC_7_Avg', 'EC_8_Avg']
VWC=['VWC_1_Avg', 'VWC_2_Avg', 'VWC_3_Avg', 'VWC_4_Avg', 'VWC_5_Avg', 'VWC_6_Avg', 'VWC_7_Avg', 'VWC_8_Avg']
T1=['T5cm_1_Avg', 'T10cm_1_Avg',  'T20cm_1_Avg',  'T30cm_1_Avg',  'T50cm_1_Avg', 'T100cm_1_Avg'  ]
T2=['T5cm_2_Avg','T10cm_2_Avg','T20cm_2_Avg','T30cm_2_Avg','T50cm_2_Avg','T100cm_2_Avg']

#select list of columns you want to plot
columns=T2
columns.reverse()

sizeParam=30,6 #change x,y size of plot

    
i=0
while (i < len(files)):
    #%%  Reads and sets up file for use by discarding unneeded columns
    file=pd.read_csv(files[i], header=[1],index_col=0)#read file i
    file=file.loc[file.index[2]:,columns].astype(float)
    file.index=pd.to_datetime(file.index)
    pivot=file.pivot_table(columns=file.index)
    pivot=pivot.reindex(index=columns)
    SoilVarDepth.soilVarDepth(pivot,title=files[i],sizeParam=sizeParam)
    i+=1