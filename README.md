# HIE
These are some scripts and things I've written as part of a contract. More to come as I get around to uploading.

***
## redfearnConversion.py
**Interactive**<br/>
Can be used for inline conversion from pandas dataframe or csv file to save as a csv or just return pandas dataframe<br/> 
Requires ‘redfearn’ library (pip install redfearn)<br/>
Uses Redfearn formula to convert Map Grid of Australia (MGA) Northings and Eastings<br/>

***
## TERNconcatanation.py
Finds all files that match CUP_S00_TERNHECT\*R.dat, validates, calibrates, and concatanates the data.<br/>
* Fixes bad quotation marks around NaN values in several files<br/>
* Plots the raw data (PA_uS_Avg(\[1-3\]) from each file in a separate color to allow visual data validation
* Uses Chelsea's soil calibrations to generate VWC(\[1-3\])<br/>
* Plots PA_uS_Avg(\[1-3\]) against the default calibration VW_Avg(\[1-3\]) and against VWC(\[1-3\]) to display the differences in calibration

