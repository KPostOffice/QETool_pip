import matplotlib.pyplot as plt
import matplotlib.dates as dt
import config
import datetime
import numpy as np


# string of form YYYY-MM-DD
def stringDateToEpoch(string):
    dateArr = string.split('-')
    dateArr = [int(x) for x in dateArr]
    return (datetime.datetime(dateArr[0], dateArr[1], dateArr[2])).timestamp()

def getData(card, test, subTest, type, epochStart, epochEnd):
    query = {
        "datetime": {
            "$lte": epochEnd,
            "$gte": epochStart
        },
        "type": type,
        "test": test,
        "cardName": card,
        "subTest": subTest
    }
    data = (config.collection.find(
        query,
        projection={
            "sheetId": True,
            "data": True,
            "datetime": True,
            "test": True,
            "subTest": True
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


def plotMany(cards, test, subTest, type, labels, start, end, fileName="test.pdf"):
    fig = plt.figure(figsize=(18,9))
    ax = fig.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
    startEpoch = stringDateToEpoch(start)
    endEpoch = stringDateToEpoch(end) + (24*60*60)
    ax.set_facecolor("#330000")
    for card in cards:
        for label in labels:
            plotData(card, label,getData(card,test,subTest,type, startEpoch, endEpoch),ax)
    (ymin, ymax) = plt.ylim()
    bottom = ymin-ymax+ymin
    top = ymax+ymax-ymin
    ax.grid(color="#6A0000", lw = 2.5)
    ax.set_title(test + ": " + subTest + " " + type)
    print(10**int(np.log10(ymax-ymin)))
    ax.set_yticks(np.arange(bottom, top, 10**int(np.log10(ymax-ymin))))
    ax.ticklabel_format(axis = 'y', style='plain', useOffset=False)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.)
    ax.set_ylim(bottom=bottom, top=top)
    plt.savefig(fileName)
    plt.close('all')
