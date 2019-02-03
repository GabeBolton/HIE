# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:08:08 2019

@author: jbgab
"""

import glob
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import SoilVarDepth

folderPath='ternsoildata\\'
files = glob.glob(folderPath+'*.dat')
infiles=[]
for file in files: 
    thisfile=pd.read_csv(file,index_col=0,skiprows=[0,2,3])
    thisfile.index=pd.to_datetime(thisfile.index)
    infiles.append(thisfile)
concat=pd.concat(infiles[:], ignore_index=False,sort=False)
concat.index=pd.to_datetime(concat.index)
#list columns that you want to plot
VW_Avg=['VW_Avg(1)', 'VW_Avg(2)', 'VW_Avg(3)', 'VW_Avg(4)']
PA=['PA_uS_Avg(1)', 'PA_uS_Avg(2)', 'PA_uS_Avg(3)', 'PA_uS_Avg(4)']
#select list of columns you want to plot
columns=VW_Avg
columns.reverse()

sizeParam=30,6 #change x,y size of plot
concat=concat.loc[:,columns]
#pivot=concat.loc[:,['VW_Avg(1)', 'VW_Avg(2)', 'VW_Avg(3)', 'VW_Avg(4)']].T.astype(float)
pivot=concat.pivot_table(columns=concat.index)
pivot=pivot.reindex(index=columns)

SoilVarDepth.soilVarDepth(pivot,title='ternsoildata',sizeParam=sizeParam,xlabel='onceamonth')

