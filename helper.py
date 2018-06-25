import matplotlib.pyplot as plt
import matplotlib.dates as dt
import config
import datetime
import numpy as np
from apiRequest import QEdataRequest

req = QEdataRequest()

# string of form YYYY-MM-DD
def stringDateToEpoch(string):
    dateArr = string.split('-')
    dateArr = [int(x) for x in dateArr]
    return (datetime.datetime(dateArr[0], dateArr[1], dateArr[2])).timestamp()


# TODO: TRANSFER THIS SERVER SIDE AS A GET REQUEST SO THAT USER DOES NOT DIRECTLY ACCESS DATABASE
def getData(card, test, subtest, type, epochStart, epochEnd):
    query = {
        "datetime": {
            "$lte": epochEnd,
            "$gte": epochStart
        },
        "type": type,
        "test": test,
        "cardName": card,
        "subtest": subtest
    }
    data = (config.collection.find(
        query,
        projection={
            "sheetId": True,
            "data": True,
            "datetime": True,
            "test": True,
            "subtest": True
        })).sort('datetime',1)
    return data

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
