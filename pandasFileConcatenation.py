import glob
import pandas as pd
folderPath=''#subpath from working directory where files are
files = glob.glob(folderPath+'*.dat')#matches all .dat files
fileData=[]
for file in files:
    fileData.append(pd.read_csv(file,index_col=0))# use skiprows=[0,1,2,5] etc. to skip rows
concat=pd.concat(fileData[:], ignore_index=False,sort=False)
