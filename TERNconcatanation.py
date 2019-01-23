# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:18:27 2019

@author: jbgab
"""
import glob
import pandas as pd
import numpy as np
folderPath='ternsoildata\\'
files = glob.glob(folderPath+'*R.dat')
infiles=[]
for file in files:
    thisfile=pd.read_csv(file,index_col=0,skiprows=[0,2,3])
    thisfile.index=pd.to_datetime(thisfile.index)
    thisfile=thisfile.replace('NaN""',np.nan)#fixing data
    thisfile=thisfile.replace('NAN""',np.nan)#fixing data
    thisfile=thisfile.astype(float)#fixing data
    thisfile.loc[:,'RECORD']=thisfile.loc[:,'RECORD'].astype(int)
    #alluvial
    #y = 0.0141x2 + 1.7623x - 28.055   assuming x2=x^2
    thisfile.loc[:,'VWC(1)']=0.0141*(thisfile.loc[:,'PA_uS_Avg(1)']*thisfile.loc[:,'PA_uS_Avg(1)'])+1.7623*thisfile.loc[:,'PA_uS_Avg(1)']-28.055
    thisfile.loc[:,'VWC(2)']=0.0141*(thisfile.loc[:,'PA_uS_Avg(2)']*thisfile.loc[:,'PA_uS_Avg(2)'])+1.7623*thisfile.loc[:,'PA_uS_Avg(2)']-28.055
    #clay
    #y = 0.0761x2 - 2.3773x + 23.195.
    thisfile.loc[:,'VWC(3)']=0.0761*(thisfile.loc[:,'PA_uS_Avg(3)']*thisfile.loc[:,'PA_uS_Avg(3)'])-2.3773*thisfile.loc[:,'PA_uS_Avg(3)']+23.195
    infiles.append(thisfile)
concat=pd.concat(infiles[:], ignore_index=False,sort=False)