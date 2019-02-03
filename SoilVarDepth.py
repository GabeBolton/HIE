# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:14:24 2018

@author: jbgab
"""
#  This 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def soilVarDepth(file,sizeParam=(3,15),title='',xlabel='midnight'):
    # Plots a pcolormesh and colourbar
    fig, (ax) = plt.subplots(figsize=sizeParam)
    c = ax.pcolormesh(file.values, edgecolors='k', linewidths=0,vmin=file.values.min(),vmax=file.values.max()) # plots pcolormesh, vmin and vmax normalize the data so the colors are scaled nicely
    ax.set_title(title) # Makes sure you know where the data came from
    fig.colorbar(c, ax=ax) # plots a colorbar (the thing on the right) to serve as a key
    #%%  This makes a good old list object for yticks and xticks because file.[index|columns] returns an object that ax.set_* dosn't like
    print('setting tick labels')
    yticks=[]
    for l in file.index:
        yticks.append(l)
    xticks=[]
    if xlabel=='midnight':
        for l in file.columns:
            if str(l.time())=='00:00:00':
                xticks.append(l)
            else:
                xticks.append('')#because it wants to show a tick at every time point
    if xlabel=='onceamonth':
        for l in file.columns:
            if (str(l.day)=='1')&(str(l.time())=='00:00:00'):
                xticks.append(l)
            else:
                xticks.append(None)#because it wants to show a tick at every time point
    #%%  This positions and assigns tick labels
    print('labeling')
    ax.set_yticks(np.arange(len(yticks)))
    ax.set_xticks(np.arange(len(xticks)))
    
    ax.set_yticklabels(yticks)
    ax.set_xticklabels(xticks)
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    
    fig.tight_layout()
    print('showing')
    plt.show()
    #%%

def sortColumns(file):# - useful for making new column lists. Type "files" to get a list of files, Then just type "sortColumns(filenumber)" into the console
    file=pd.read_csv(file, header=[1],index_col=0)#read file i    
    file=file.reindex(sorted(file.columns), axis=1)#sort file i columns
    print(file.columns)#print sorted list