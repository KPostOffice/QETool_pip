from config import structure
import graph
from matplotlib.backends.backend_pdf import PdfPages
import regexHelp
import re

validPdfName = r'^\w+\.pdf$'
validDate = r'^\d{4}\-(0[1-9]|1[0-2])\-([0-2]\d|3[0-1])$'

class MultiGraph():
    def __init__(self, fileName):
        self.fileName = fileName
        self.pdfName = ""
        self.graphs = []

    def construct(self):
        lineNum = 1
        pdfName = ""
        graphs = []   # new empty non-instance variables allow for nonassignment if input is invalid
        options = []
        fileOb = open(self.fileName, "r")
        pdfName = fileOb.readline().rstrip()
        # TODO: Pdf name with regular expression or raise an error
        if(not re.match(validPdfName, pdfName)):
            message = "Line {0:d}: {} is not a valid name for a pdf please have it of form \w+.pdf"
            raise IOError(message.format(lineNum, fileName))

        lineNum = 2

        for line in fileOb:
            line = line.rstrip()
            options = line.split(':')

            if(len(options)<7):
                message = "Line {}: Not enough arguments provided, needed 7 or 8 seperated by ':' but got {}"
                raise IOError(message.format(lineNum, len(options)))
            elif(len(options)>8):
                message = "Line {}: Too many arguments provided, needed 7 or 8 seperated by ':' but got {}"
                raise IOError(message.format(lineNum, len(options)))

            cards = set(options[0].split(','))
            cardReg = regexHelp.cardsRegex()

            for card in cards:
                if(not re.match(cardReg,card)):
                    message = "Line {}: {} is not a valid card name. Valid names are: {}"
                    raise IOError(message.format(lineNum, card, ', '.join(structure[cards])))

            test = options[1]
            testReg = regexHelp.testsRegex()

            if(not re.match(testReg, test)):
                message = "Line {}: {} is not a valid test name"
                raise IOError(message.format(lineNum))

            subTest = options[2]
            subTestReg = regexHelp.subTestsRegex(test)

            if(not re.match(subTestReg, subTest)):
                message = "Line {}: {} is not a valid subTest choice with current selection: test={}"
                raise IOError(message.format(lineNum, subTest, test))

            type = options[3]
            typeReg = regexHelp.typeRegex(test, subTest)

            if(not re.match(typeReg, type)):
                message = "Line {}: {} is not a valid type option with current selection: test={}, subTest={}"
                raise IOError(message.format(lineNum,type, test, subTest))

            labels = set(options[4].split(','))

            labelReg = regexHelp.labelsRegex(test,subTest,type)

            for label in labels:
                if(not re.match(labelReg,label)):
                    message = "Line {}: {} is not a valid label option with current selection: test={}, subTest={}, type={}"
                    raise IOError(message.format(lineNum,label,test,subTest,type))

            start = options[5]

            if(not re.match(validDate, start)):
                message = "Line {}: {} is not a valid format for start date"
                raise IOError(message.format(lineNum,start))

            end = options[6]

            if(not re.match(validDate, end)):
                message = "Line {}: {} is not a valid format for end date"
                raise IOError(message.format(lineNum,end))

            graphs.append(graph.Graph(cards, test, subTest, type, labels, start, end))
        self.graphs = graphs
        self.pdfName = pdfName

    def createBook(self):
        with PdfPages(self.pdfName) as pdf:
            for graph in self.graphs:
                graph.plotGraph(multiPdf=pdf)
