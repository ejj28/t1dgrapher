# t1dgrapher

#### I WILL NOT BE HELD RESPONSIBLE FOR ANYTHING CAUSED BY THE USE OF THIS SOFTWARE. THIS SOFTWARE SHOULD NOT BE USED TO MAKE ANY MEDICAL DECISIONS AND IN THE EVENT THAT IT IS I WILL NOT BE HELD RESPONSIBLE FOR ANY MEDICAL ISSUES. FOR MORE INFORMATION, PLEASE SEE THE LICENSE.

Medtronic Pump &amp; Dexcom CGM Data Grapher 

Takes a Medtronic export CSV and a Diasend export XLS, and graphs the Dexcom CGM data and the Medtronic Pump Data.

### Usage

python core.py diasend.xls medtronic.csv outputfile.html

Currently for some reason the outputted html file containing the Plotly graph does not use the filename that the user specifies. However, not specifying a name at all crashes the program.
