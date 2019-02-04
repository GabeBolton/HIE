# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:31:40 2019

@author: jbgab
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:37:23 2018

@author: jbgab
"""

import matplotlib.pyplot as plt
import pandas as pd

def spatial(x,y,c,title=''):
    maxX=max(x)
    minX=min(x)
    xdev=(maxX-minX)
    #xlim=xdev*.05
    xbound=xdev
    while xbound < 5:
        xbound+=xdev*(5-int(xbound))
    xbound=int(xbound)
    
    maxY=max(y)
    minY=min(y)
    ydev=(maxY-minY)
    #ylim=xdev*.05
    #ybound=ydev
    ybound=xbound*(ydev/xdev)
    ybound=int(ybound)
    
    figsize=(xbound,ybound)
    plt.title=(title)

    plt.figure(figsize=figsize,dpi=100)
    plt.xlim(minX-xdev,maxX+xdev)
    plt.ylim(minY-ydev,maxY+ydev)

    plt.scatter(x,y,s=10,c=c)
    plt.ticklabel_format(style='plain',axis='both', useOffset=False)
    
    plt.axis('equal')
    plt.grid(True)
    plt.show()


#%%  Example of use


lonColumn='Lon'
latColumn='Lat'

soilsensors = pd.read_csv('eucfacesoilsensorfiles\\convertedLocations.csv',index_col=0)
soilsensors=soilsensors.rename(columns={'Latitude':latColumn,'Longitude':lonColumn})
#soilsensorsCleaned=soilsensors.loc[[lonColumn,latColumn],:].values.astype(float)
soils = pd.read_csv('sensorLocations.csv_out.csv',index_col=0)
ringColler=pd.read_csv('out_EucFACE_exact_mapgrid_ring_coller.csv',index_col=0)
locations = pd.concat([soilsensors, soils,ringColler], ignore_index=True,sort=False)
locations.index=locations.UniqueID

import glob
import re
#files like FACE_R1_B1_SoilVars_20180831.dat
filePath='eucfacesoilsensorfiles\\'
outPath='eucfacesoilsensorFigures\\'
files = glob.glob(filePath+'*SoilVars*.dat')#uses psuedo regex to access a list of files
print(files)

testing=True

i=0
while (i < len(files)):
    title=files[i].strip(filePath)
    file=pd.read_csv(files[i], header=[1],index_col=0)#read file i
    plotterVals=file.loc[file.index[2]:,file.columns[1]:].astype(float)
    plotterVals.index=pd.to_datetime(plotterVals.index)
    ring=float(re.findall('R([0-9])',title)[0])
    currentlocations=locations[locations.loc[:,'Ring']==ring]
    minimum=dict()
    maximum=dict()
    deviation=dict()
    for column in plotterVals:
        minimum[column]=plotterVals[column].min()
        maximum[column]=plotterVals[column].max()
        deviation[column]=plotterVals[column].max()-plotterVals[column].min()
    x=[]
    y=[]
    c=[]
    for timestamp,data in plotterVals.iterrows():
        i=0
        while i<len(data):
            try:
                sensorname=data.index[i]
                normalizedsensor=(data[i]-minimum[sensorname])/deviation[sensorname]
                x.append(currentlocations.loc[sensorname,lonColumn].values[0].astype(float))
                y.append(currentlocations.loc[sensorname,latColumn].values[0].astype(float))
                c.append(normalizedsensor)
            except:
                e=1
            i+=1
        spatial(x,y,c,title=str(timestamp))
        
        
    i+=1

