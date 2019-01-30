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
* Plots the raw data (PA_uS_Avg(\[1-3\]) from each file in a separate color to allow visual data validation. This assisted in the diagnosis of sensor issues (large streaks in TERN_PA_uS_Avg(\[1-\3]).png)<br>
![Alt text](https://raw.githubusercontent.com/GabeBolton/HIE/master/TERN_PA_uS_Avg(%5B1-3%5D).png?raw=true "TERN_PA_uS_Avg([1-3].png")<br>
* Uses Chelsea's soil calibrations to generate VWC(\[1-3\])<br/>
* Plots PA_uS_Avg(\[1-3\]) against the default calibration VW_Avg(\[1-3\]) and against VWC(\[1-3\]) to display the differences in calibration and highlights negative values caused by data errors (TERN_PA_vs_VW.png)
![Alt text](https://raw.githubusercontent.com/GabeBolton/HIE/master/TERN_PA_vs_VW.png?raw=true "TERN_PA_vs_VW.png")

***
## TERN work summary
Here is a brief summary of what I have done.<br/>
<details>
  <summary>Fixed Data Format of 20151019-20151124</summary>
  <p>

Using regular expressions (henceforth regex) I changed CUP_S00_TERNHECT_616_20151019-20151124_R.dat from:
<pre><code>
"TOA5,""Plot 7 Soil Moisture Campaign"",""CR1000"",""42701"",""CR1000.Std.22"",""CPU:PARunderstory10082015.CR1"",""9508"",""CUP_S00_TERNHECT_616"""
"TIMESTAMP,""RECORD"",""VW_Avg(1)"",""VW_Avg(2)"",""VW_Avg(3)"",""VW_Avg(4)"",""PA_uS_Avg(1)"",""PA_uS_Avg(2)"",""PA_uS_Avg(3)"",""PA_uS_Avg(4)"",""T107_C(1)"",""T107_C(2)"",""T107_C(3)"""
"TS,""RN"","""","""","""","""","""","""","""","""","""","""","""""
","""",""Avg"",""Avg"",""Avg"",""Avg"",""Avg"",""Avg"",""Avg"",""Avg"",""Smp"",""Smp"",""Smp"""
"2015-10-19 11:30:00,2970,0.059,0.289,0.002,0.136,18.6,27.48,15.33,22.09,20.9,19.37,18.44"
"2015-10-19 12:00:00,2971,0.059,0.29,0.001,0.135,18.6,27.49,15.31,22.04,21.47,19.53,18.45"
"2015-10-19 12:30:00,2972,0.059,0.29,0.001,0.133,18.6,27.5,15.3,21.95,21.88,19.76,18.47"
"2015-10-19 13:00:00,2973,0.059,0.29,0.001,0.129,18.61,27.52,15.27,21.81,21.99,19.95,18.49"

...etc.
</code></pre>
To:

<pre><code>
"TOA5","Plot 7 Soil Moisture Campaign"",""CR1000"",""42701"",""CR1000.Std.22"",""CPU:PARunderstory10082015.CR1"",""9508"",""CUP_S00_TERNHECT_616"""
"TIMESTAMP","RECORD","VW_Avg(1)","VW_Avg(2)","VW_Avg(3)","VW_Avg(4)","PA_uS_Avg(1)","PA_uS_Avg(2)","PA_uS_Avg(3)","PA_uS_Avg(4)","T107_C(1)","T107_C(2)","T107_C(3)"
"TS","RN","","","","","","","","","","",""
"","","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Smp","Smp","Smp"
"2015-10-19 11:30:00",2970,0.059,0.289,0.002,0.136,18.6,27.48,15.33,22.09,20.9,19.37,18.44
"2015-10-19 12:00:00",2971,0.059,0.29,0.001,0.135,18.6,27.49,15.31,22.04,21.47,19.53,18.45
"2015-10-19 12:30:00",2972,0.059,0.29,0.001,0.133,18.6,27.5,15.3,21.95,21.88,19.76,18.47
"2015-10-19 13:00:00",2973,0.059,0.29,0.001,0.129,18.61,27.52,15.27,21.81,21.99,19.95,18.49

...etc.
</code></pre>
Making it consistent with the format of CUP_S00_TERNHECT_616_20150818_20151019_R.dat<br>
There are two errors, one in the headers shown on the very first line: <code>"TOA5,""Plot 7 Soil Moisture Campaign"",""CR1000"", etc </code><br>
look at that again: "TOA5,~~""~~ Plot 7 Soil Moisture Campaign ~~""~~,~~""~~ CR1000 ~~""~~ etc <br>
That goes on for the rest of the header lines, so because the data layout is consistant I used the header from CUP_S00_TERNHECT_616_20150818_20151019_R.dat, however replace it after dealing with the next issue: the data.<br>
The data lines have a <code>"</code> at the start and end of the lines, instead of at the start and end of the timestamp. To fix this
use notepad++, Visual Studio Code or any other text proccessor with regex find and replace<br>
find: <code>"\n</code><br>
replace: <code>\n</code><br>
then<br>
find: <code>0:00,</code><br>
replace: <code>0:00",</code><br>
</p>
</details>
<details>
  <summary>Fixed Bad Quote NaN values</summary>

Several files had issues in columns ‘VW_Avg(4)’ and ‘PA_uS_Avg(4)’ with NaN values being recorded as ‘NAN””’, those are fixed with TERNconcatanation in python with <code>pandas.Dataframe.replace(‘NAN””’,np.nan)</code> with <code>thisfile=thisfile.replace('NAN""',np.nan)</code>

</details>

<details>
  <summary>Plotting Raw Data</summary>
Plots the raw data (PA_uS_Avg(\[1-3\]) from each file in a separate color to allow visual data validation. This assisted in the diagnosis of sensor issues (large streaks in TERN_PA_uS_Avg(\[1-\3]).png)<br>
![Alt text](https://raw.githubusercontent.com/GabeBolton/HIE/master/TERN_PA_uS_Avg(%5B1-3%5D).png?raw=true "TERN_PA_uS_Avg([1-3].png")<br>
</details>


<details>
  <summary>Calibration & Validation</summary>
  Used Chelsea's soil calibrations to generate VWC(\[1-3\]) in TERNconcatanation.py:<br>
  alluvial: <code>y = 0.0141x<sup>2</sup> + 1.7623x - 28.055</code><br>
  clay: <code>y = 0.0761x<sup>2</sup> - 2.3773x + 23.195</code><br>
  VWC(\[1-2\]) uses alluvial; VWC(3) uses clay<br>
Plots PA_uS_Avg(\[1-3\]) against the default calibration VW_Avg(\[1-3\]) and against VWC(\[1-3\]) to display the differences in calibration and highlights negative values caused by data errors (TERN_PA_vs_VW.png)
![Alt text](https://raw.githubusercontent.com/GabeBolton/HIE/master/TERN_PA_vs_VW.png?raw=true "TERN_PA_vs_VW.png")

</details>

<details>
  <summary>Noise Trimming</summary>
Added in noise trimming functionality to trim data below user-defined threshold to remove the noise shown in TERN_PA_uS_Avg([1-3]).png as large streaks, and in TERN_PA_vs_VW.png as out of equation data on VW_Avg (not on line) and out of bounds data on VWC (below 0 as a hard lower bound). This method is not as beautiful as other methods such as rejecting data outside of bounds determined by previous datapoints, but it is more reproducable and transparent.
</details>
