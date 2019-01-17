# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:25:41 2018
@author: Gabe Bolton
Input file format: 'easting', 'northing'
Output file format:  'easting', 'northing', 'lat', 'lon'
"""
import redfearn
import pandas as pd

def rc_ie_RedFearnConverter(inFile='',outFile='',save='',easting='easting',northing='northing',latatude='lat',longitude='lon' ):
    #%% UI Chod
    print("Program by Gabe Bolton, based on the redfearn python library (pip install redfearn) \nInput file format: csv with headers: "+easting+', '+northing)
    if (easting=='easting')&(northing=='northing')&(latatude=='lat')&(longitude=='lon'):
        print("\nFun fact, you can change the column names by calling rc_ie_RedFearnConverter() in the command line.\n\nFor example if your Northings are in a column called 'northings' you can type: \nrc_ie_RedFearnConverter(northing='northings')\nIf your eastings column is also called 'eastings' you would type: \nrc_ie_RedFearnConverter(northing='northings',eastings='eastings')\nAnd so on for each of your columns")
    if inFile=='':
        inFile = input("Please enter Input filename: ")
        print('Next time you can also use a pandas dataframe as inFile')
    if save!=False:
        if save!=True:
            saveInput=input("do you want to save the converted file? y/n    ")
            if (saveInput=='y')|(saveInput=='Y'):
                save=True
        if save==True:
            if outFile=='':
                outfile = inFile+'_out.csv'
            print('outfile: '+outfile)
    if type(inFile) is not pd.core.frame.DataFrame:
        data = pd.read_csv(inFile)
    #%% Active ingredient
    i=0
    while i < data.shape[0]:
        redFormula=(redfearn.grid2latlon(data.loc[i,easting], data.loc[i,northing],56))  
        data.loc[i,latatude] = redFormula.get('latitude')
        data.loc[i,longitude] = redFormula.get('longitude')
        i+=1
    if save==True:
        data.to_csv(outfile)
    return data #this allows you to call it inline to be able to use the pandas dataframe

rc_ie_RedFearnConverter()