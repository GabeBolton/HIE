import glob
import pandas as pd
folderPath=''#subpath from working directory where files are
file = glob.glob(folderPath+'\\*.dat')#matches all .dat files
fileData=[]
for file in files:
    fileData.append(pd.read_csv(file,index_col=0,skiprows=[0,2,3]))
concat=pd.concat(fileData[:], ignore_index=False,sort=False)
