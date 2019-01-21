# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:33:56 2019

@author: jbgab
"""

import glob
import pandas as pd
import numpy as np

def plotIt(file,columns,append='',title='',save=False,outPath='',plotSeparatly=True,sizeParam=(10,3)):
    
    plotterVals=file.loc[:,columns]
    plotterVals.index=pd.to_datetime(plotterVals.index)
    plotted=plotterVals.plot(use_index=True,title=(title+append),subplots=plotSeparatly,figsize=sizeParam)
    if save:
        fig=plotted[0].get_figure()
        filename=outPath+title+append+'.png'
        fig.savefig(filename,bbox_inches='tight')

folderPath='ternsoildata\\'
files = glob.glob(folderPath+'*.dat')
infiles=[]
for file in files: 
    thisfile=pd.read_csv(file,index_col=0,skiprows=[0,2,3])
    thisfile.index=pd.to_datetime(thisfile.index)
    thisfile=thisfile.replace('NaN""',np.nan)#fixing data
    thisfile=thisfile.replace('NAN""',np.nan)#fixing data
    thisfile=thisfile.astype(float)#fixing data
    infiles.append(thisfile)
concat=pd.concat(infiles[:], ignore_index=False,sort=False)
concat.index=pd.to_datetime(concat.index)
#list columns that you want to plot
VW_Avg=['VW_Avg(1)', 'VW_Avg(2)', 'VW_Avg(3)', 'VW_Avg(4)']
PA=['PA_uS_Avg(1)', 'PA_uS_Avg(2)', 'PA_uS_Avg(3)', 'PA_uS_Avg(4)']
#select list of columns you want to plot
columns=VW_Avg

sizeParam=30,10 #change x,y size of plot

plotIt(concat,columns=concat.columns,title='',sizeParam=sizeParam,plotSeparatly=True)
