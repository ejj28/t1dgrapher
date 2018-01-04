#!/usr/bin/env python

import plotly
import plotly.graph_objs as go
from datetime import datetime
import pandas
import sys

def generateGraph(cgmInputFile, pumpInputFile, outputFilename):

    cgmx = []
    cgmy = []
    pumpy = []
    pumpx = []
    goodindex = []
    count = 0
    cgmcountx = 0
    cgmcounty = 0
    pc = 0
    cgmcsv = pandas.read_excel(str(cgmInputFile), sheetname='CGM', header=None)  # pandas.read_csv(str(sys.argv[1]), header=None)
    for i in cgmcsv[0]:
        if cgmcountx == 0:
            cgmcountx = cgmcountx + 1
            continue
        elif cgmcountx == 1:
            cgmcountx = cgmcountx + 1
            continue
        else:
            a = datetime.strptime(i, '%d/%m/%Y %H:%M')
            cgmx.append(a)
            cgmcountx = cgmcountx + 1

    for i in cgmcsv[1]:
        if cgmcounty == 0:
            cgmcounty = cgmcounty + 1
            continue
        elif cgmcounty == 1:
            cgmcounty = cgmcounty + 1
            continue
        else:
            cgmy.append(round(float(i) * 2) / 2)
            cgmcounty = cgmcounty + 1
    cgm = go.Scatter(
        x = cgmx,
        y = cgmy,
        mode = 'lines+markers',
        name = 'CGM'
    )

    pumpcsv = pandas.read_csv(str(pumpInputFile), header=None, skiprows=12, sep=None)

    for i in pumpcsv[33]:
        if i == 'BolusNormal':
            goodindex.append(count)
        count = count + 1

    for i in goodindex:
        #print i
        pumpx.append(datetime.strptime(pumpcsv[3][i], '%d/%m/%y %H:%M:%S'))
        pumpy.append(pumpcsv[11][i])


    pump = go.Scatter(
        x = pumpx,
        y = pumpy,
        mode = 'markers',
        name = 'Bolus'
    )

    data = [cgm, pump]
    plotly.offline.plot(data, str(outputFilename))


generateGraph(sys.argv[1], sys.argv[2], sys.argv[3])
