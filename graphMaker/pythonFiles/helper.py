import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime
import numpy as np
from apiRequest import QEdataRequest

req = QEdataRequest()

# string of form YYYY-MM-DD
def stringDateToEpoch(string):
    dateArr = string.split('-')
    dateArr = [int(x) for x in dateArr]
    return (datetime.datetime(dateArr[0], dateArr[1], dateArr[2])).timestamp()

def plotData(card, label, data, ax):
    x=[]
    y=[]
    for datum in data:
        if datum['data'] != None and label in datum['data']:
            x.append((dt.seconds(datum['datetime'])+365.25*1969))
            y.append(dt.epoch2num(datum['data'][label]))
    ax.plot_date(x,y,'-o', label = card + ' ' + label)

def regFromList(list):
    return r'^(' + r'|'.join(list) + r')$'
