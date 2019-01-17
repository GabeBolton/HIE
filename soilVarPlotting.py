# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 07:59:20 2018

@author: jbgab
"""

import glob
import pandas as pd

save=False
sizeparam=20,6 #change x,y size of plot
separatePlots=1 #plot separatly or together

filePath='eucfacesoilsensorfiles\\'
outPath='eucfacesoilsensorFigures\\'
files = glob.glob(filePath+'*SoilVars*.dat')#uses regex to access a list of files
print(files)

#list columns that you want to plot, generate new column lists with sortColumns(i)
theta1=['Theta5_1_Avg', 'Theta30_1_Avg', 'ThetaHL_1_Avg','Theta75_1_Avg']
theta2=['Theta5_2_Avg', 'Theta30_2_Avg', 'ThetaHL_2_Avg','Theta75_2_Avg']
TDR=['TDRTemp_1_Avg', 'TDRTemp_2_Avg','TDRTemp_3_Avg', 'TDRTemp_4_Avg', 'TDRTemp_5_Avg', 'TDRTemp_6_Avg','TDRTemp_7_Avg', 'TDRTemp_8_Avg']
T=['T100cm_1_Avg', 'T100cm_2_Avg', 'T10cm_1_Avg', 'T10cm_2_Avg', 'T20cm_1_Avg', 'T20cm_2_Avg', 'T30cm_1_Avg', 'T30cm_2_Avg', 'T50cm_1_Avg', 'T50cm_2_Avg', 'T5cm_1_Avg', 'T5cm_2_Avg']
EC=['EC_1_Avg', 'EC_2_Avg', 'EC_3_Avg', 'EC_4_Avg', 'EC_5_Avg', 'EC_6_Avg','EC_7_Avg', 'EC_8_Avg']
VWC=['VWC_1_Avg', 'VWC_2_Avg', 'VWC_3_Avg', 'VWC_4_Avg', 'VWC_5_Avg', 'VWC_6_Avg', 'VWC_7_Avg', 'VWC_8_Avg']
T1=['T5cm_1_Avg', 'T10cm_1_Avg',  'T20cm_1_Avg',  'T30cm_1_Avg',  'T50cm_1_Avg', 'T100cm_1_Avg'  ]
T2=['T5cm_2_Avg','T10cm_2_Avg','T20cm_2_Avg','T30cm_2_Avg','T50cm_2_Avg','T100cm_2_Avg']

def plotIt(file,columns,append):
    plotterVals=file.loc[file.index[2]:,columns].astype(float)
    plotterVals.index=pd.to_datetime(plotterVals.index)
    plotted=plotterVals.plot(use_index=True,title=(title+append),subplots=separatePlots,figsize=sizeparam)
    if save:
        fig=plotted[0].get_figure()
        filename=outPath+title+append+'.png'
        fig.savefig(filename,bbox_inches='tight')

i=0
while (i < len(files)):
    title=files[i].strip(filePath)
    file=pd.read_csv(files[i], header=[1],index_col=0)#read file i
    #file=file.reindex(sorted(file.columns), axis=1)#sort file i - useful for making new column lists: copy this and the above

    
    #tell it what columns lists you want to plot and what you want them to be called, ex: plotIt(file,theta1,'_theta1')    
    
    i+=1

   
def sortColumns(i):# - useful for making new column lists just type "sortColumns(number)" into the console
    file=pd.read_csv(files[i], header=[1],index_col=0)#read file i    
    file=file.reindex(sorted(file.columns), axis=1)#sort file i columns
    print(file.columns)#print sorted list
