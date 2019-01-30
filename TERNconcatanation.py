# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:18:27 2019

@author: jbgab
"""
import glob
import pandas as pd
import numpy as np
folderPath='ternsoildata\\'#path of data folder in relation to path of script, if data is in same folder as script just use ''
files = glob.glob(folderPath+'CUP_S00_TERNHECT*R.dat')
print("If you get the error: 'Unknown string format:', '2015-10-19... etc the unquote that should be at the end of the time string is at the end of the data row. Use the fixed files.")
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
    
    #plot
    plt.subplot(3,1,1)
    plt.plot(thisfile.index,thisfile.loc[:,'PA_uS_Avg(1)'])
    plt.title('PA_uS_Avg(1)')
    plt.ylim(-1,40)
    plt.grid(True)
    plt.subplot(3,1,2)
    plt.plot(thisfile.index,thisfile.loc[:,'PA_uS_Avg(2)'])
    plt.title('PA_uS_Avg(2)')
    plt.ylim(-1,40)
    plt.grid(True)
    plt.subplot(3,1,3)
    plt.plot(thisfile.index,thisfile.loc[:,'PA_uS_Avg(3)'])
    plt.title('PA_uS_Avg(3)')
    plt.ylim(-1,40)
    plt.grid(True)
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

#noise trimming
trimmed=concat[concat.loc[:,'PA_uS_Avg(1)']>15]
trimmed=trimmed[(trimmed.loc[:,'PA_uS_Avg(2)']>15)]
trimmed=trimmed[(trimmed.loc[:,'PA_uS_Avg(3)']>15)]

plt.subplots(figsize=[10,10])
plt.subplot(321)
plt.scatter(trimmed.loc[:,'PA_uS_Avg(1)'],trimmed.loc[:,'VW_Avg(1)'],marker='.',s=1)
plt.title('trimmed   x: PA_uS_Avg(1), y: VW_Avg(1)')
plt.subplot(322)
plt.scatter(trimmed.loc[:,'PA_uS_Avg(1)'],trimmed.loc[:,'VWC(1)'],marker='.',s=1)
plt.title('trimmed   x: PA_uS_Avg(1), y: VWC(1)')

plt.subplot(323)
plt.scatter(trimmed.loc[:,'PA_uS_Avg(2)'],trimmed.loc[:,'VW_Avg(2)'],marker='.',s=1)
plt.title('trimmed   x: PA_uS_Avg(2), y: VW_Avg(2)')
plt.subplot(324)
plt.scatter(trimmed.loc[:,'PA_uS_Avg(2)'],trimmed.loc[:,'VWC(2)'],marker='.',s=1)
plt.title('trimmed   x: PA_uS_Avg(2), y: VWC(2)')

plt.subplot(325)
plt.scatter(trimmed.loc[:,'PA_uS_Avg(3)'],trimmed.loc[:,'VW_Avg(3)'],marker='.',s=1)
plt.title('trimmed   x: PA_uS_Avg(3), y: VW_Avg(3)')
plt.subplot(326)
plt.scatter(trimmed.loc[:,'PA_uS_Avg(3)'],trimmed.loc[:,'VWC(3)'],marker='.',s=1)
plt.title('trimmed   x: PA_uS_Avg(3), y: VWC(3)')

plt.subplots(figsize=[30,10])
plt.subplot(3,1,1)
plt.scatter(trimmed.index,trimmed.loc[:,'PA_uS_Avg(1)'],marker='.',s=1)
plt.title('trimmed PA_uS_Avg(1)')
plt.ylim(-1,40)
plt.grid(True)
plt.subplot(3,1,2)
plt.scatter(trimmed.index,trimmed.loc[:,'PA_uS_Avg(2)'],marker='.',s=1)
plt.title('trimmed PA_uS_Avg(2)')
plt.ylim(-1,40)
plt.grid(True)
plt.subplot(3,1,3)
plt.scatter(trimmed.index,trimmed.loc[:,'PA_uS_Avg(3)'],marker='.',s=1)
plt.title('trimmed PA_uS_Avg(3)')
plt.ylim(-1,40)
plt.grid(True)
