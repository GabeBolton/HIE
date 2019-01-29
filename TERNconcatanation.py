# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:18:27 2019

@author: jbgab
"""
import glob
import pandas as pd
import numpy as np
folderPath='ternsoildata\\'
files = glob.glob(folderPath+'CUP_S00_TERNHECT*R.dat')
infiles=[]
for file in files:
    thisfile=pd.read_csv(file,index_col=0,skiprows=[0,2,3])
    thisfile.index=pd.to_datetime(thisfile.index)
    thisfile=thisfile.replace('NaN""',np.nan)#fixing data
    thisfile=thisfile.replace('NAN""',np.nan)#fixing data
    thisfile=thisfile.astype(float)#fixing data
    thisfile.loc[:,'RECORD']=thisfile.loc[:,'RECORD'].astype(int)
    
    #calibration
    #alluvial
    #y = 0.0141x2 + 1.7623x - 28.055   assuming x2=x^2
    thisfile.loc[:,'VWC(1)']=0.0141*(thisfile.loc[:,'PA_uS_Avg(1)']*thisfile.loc[:,'PA_uS_Avg(1)'])+1.7623*thisfile.loc[:,'PA_uS_Avg(1)']-28.055
    thisfile.loc[:,'VWC(2)']=0.0141*(thisfile.loc[:,'PA_uS_Avg(2)']*thisfile.loc[:,'PA_uS_Avg(2)'])+1.7623*thisfile.loc[:,'PA_uS_Avg(2)']-28.055
    #clay
    #y = 0.0761x2 - 2.3773x + 23.195.
    thisfile.loc[:,'VWC(3)']=0.0761*(thisfile.loc[:,'PA_uS_Avg(3)']*thisfile.loc[:,'PA_uS_Avg(3)'])-2.3773*thisfile.loc[:,'PA_uS_Avg(3)']+23.195
    
    infiles.append(thisfile)
concat=pd.concat(infiles[:], ignore_index=False,sort=False)

#testing data calibration
plt.subplots(figsize=[10,10])
plt.subplot(321)
plt.scatter(concat.loc[:,'PA_uS_Avg(1)'],concat.loc[:,'VW_Avg(1)'],marker='.',s=1)
plt.title('x: PA_uS_Avg(1), y: VW_Avg(1)')
plt.subplot(322)
plt.scatter(concat.loc[:,'PA_uS_Avg(1)'],concat.loc[:,'VWC(1)'],marker='.',s=1)
plt.title('x: PA_uS_Avg(1), y: VWC(1)')

plt.subplot(323)
plt.scatter(concat.loc[:,'PA_uS_Avg(2)'],concat.loc[:,'VW_Avg(2)'],marker='.',s=1)
plt.title('x: PA_uS_Avg(2), y: VW_Avg(2)')
plt.subplot(324)
plt.scatter(concat.loc[:,'PA_uS_Avg(2)'],concat.loc[:,'VWC(2)'],marker='.',s=1)
plt.title('x: PA_uS_Avg(2), y: VWC(2)')

plt.subplot(325)
plt.scatter(concat.loc[:,'PA_uS_Avg(3)'],concat.loc[:,'VW_Avg(3)'],marker='.',s=1)
plt.title('x: PA_uS_Avg(3), y: VW_Avg(3)')
plt.subplot(326)
plt.scatter(concat.loc[:,'PA_uS_Avg(3)'],concat.loc[:,'VWC(3)'],marker='.',s=1)
plt.title('x: PA_uS_Avg(3), y: VWC(3)')
