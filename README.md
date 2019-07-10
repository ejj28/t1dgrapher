# t1dgrapher

## Bolus &amp; CGM Data Grapher

#### :warning:Please be careful when using this! t1dgrapher shouldn't be used to make medical decisions!:warning:

### Supported devices:

#### CGMs:

* Dexcom G5 (through Diasend)

#### Pumps:

* Medtronic MiniMed
* Tandem T:Slim hopefully coming soon!

### Usage

You'll need to export your Medtronic data to a csv file and to export your Dexcom data to an xls through Diasend

Then run

`python core.py diasend.xls medtronic.csv outputfile.html`

Currently for some reason the outputted html file containing the Plotly graph does not use the filename that the user specifies. However, not specifying a name at all crashes the program.

Contributions are always welcome, especially since I have limited hardware to test on.
