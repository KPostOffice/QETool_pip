import helper
import matplotlib.pyplot as plt
import numpy as np

class Graph():
    """docstring for [object Object]."""
    def __init__(self, cards, test, subTest, type, labels, start, end):
        super().__init__()
        self.cards = cards
        self.test = test
        self.subTest = subTest
        self.type = type
        self.labels = labels
        self.start = start
        self.end = end

    def plotGraph(self, fileName="test.pdf", multiPdf=None):
        fig = plt.figure(figsize=(18,9))
        ax = fig.add_subplot(111, position=[0.1, 0.1, 0.8, 0.8])
        startEpoch = helper.stringDateToEpoch(self.start)
        endEpoch = helper.stringDateToEpoch(self.end) + (24*60*60)
        ax.set_facecolor("#330000")
        for card in self.cards:
            for label in self.labels:
                helper.plotData(card, label,helper.getData(card,self.test,self.subTest,self.type, startEpoch, endEpoch),ax)
        (ymin, ymax) = plt.ylim()
        bottom = ymin-ymax+ymin
        top = ymax+ymax-ymin
        ax.grid(color="#6A0000", lw = 2.5)
        ax.set_title(self.test + ": " + self.subTest + " " + self.type)
        ax.set_yticks(np.arange(bottom, top, 10**int(np.log10(ymax-ymin))))
        ax.ticklabel_format(axis = 'y', useOffset=False)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.)
        ax.set_ylim(bottom=bottom, top=top)
        if(multiPdf != None):
            multiPdf.savefig()
        else:
            plt.savefig(fileName)

        plt.close('all')
