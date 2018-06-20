import re
import config
import graph
from matplotlib.backends.backend_pdf import PdfPages


validPdfName = r'^\w+\.pdf$'
validDate = r'^\d{4}\-(0[1-9]|1[0-2])\-([0-2]\d|3[0-1])$'

class multiGraph():
    def __init__(fileName):
        self.fileName = fileName
        self.pdfName = ""
        self.graphs = []

    def construct(self):
        lineNum = 1
        pdfName = ""
        graphs = []   # new empty non-instance variables allow for nonassignment if input is invalid
        options = []
        fileOb = open(self.fileName, "r")
        pdfName = file_ob.readline().rstrip()
        # TODO: Pdf name with regular expression or raise an error
        if(not re.match(validPdfName, pdfName)):
            message = "Line {0:d}: {} is not a valid name for a pdf please have it of form \w+.pdf"
            raise IOError(message.format(lineNum, fileName))

        lineNum = 2

        for line in file_ob:
            line = line.rstrip()
            options = line.split(':')

            if(len(options)<7):
                message = "Line {0:d}: Not enough arguments provided, needed 7 or 8 seperated by ':' but got {0:d}"
                raise IOError(message.format(lineNum, len(options)))
            else if(len(options)>8):
                message = "Line {0:d}: Too many arguments provided, needed 7 or 8 seperated by ':' but got {0:d}"
                raise IOError(message.format(lineNum, len(options)))

            cards = set(options[0].split(','))
            cardReg = config.cardsRegex()

            for card in cards:
                if(not re.match(cardReg,card))
                    message = "Line {0:d}: {} is not a valid card name. Valid names are: {}"
                    raise IOError(message.format(lineNum, card, ', '.join(config.structure[cards])))

            test = options[1]
            testReg = config.testsRegex()

            if(not re.match(testReg, test)):
                message = "Line {0:d}: {} is not a valid test name"
                raise IOError(message.format(lineNum))

            subTest = options[2]
            subTestReg = config.subTestsRegex(test)

            if(not re.match(subTestReg, subTest)):
                message = "Line {0:d}: {} is not a valid subTest choice with current selection: test={}"
                raise IOError(message.format(lineNum, subTest, test))

            type = options[3]
            typeReg = config.typeRegex(test, subTest)

            if(not re.match(typeReg, type)):
                message = "Line {0:d}: {} is not a valid type option with current selection: test={}, subTest={}"
                raise IOError(message.format(lineNum,type, test, subTest))

            labels = set(options[4].split(','))
            labelReg = config.labelsRegex(test,subTest,type)

            for label in labels:
                if(not re.match(labelReg,label)):
                    message = "Line {0:d}: {} is not a valid label option with current selection: test={}, subTest={}, type={}"
                    raise IOError(message.format(lineNum,label,test,subTest,type))

            start = options[5]

            if(not re.match(validDate, start)):
                message = "Line {0:d}: {} is not a valid format for start date"
                raise IOError(message.format(lineNum,start))

            end = options[6]

            if(not re.match(validDate, end)):
                message = "Line {0:d}: {} is not a valid format for end date"
                raise IOError(message.format(lineNum,end))

            self.graphs.append(graph.Graph(cards, test, subTest, type, labels, start, end))

    def createBook(self):
        with PdfPages(self.pdfName) as pdf:
            for graph in self.graphs:
                graph.plotGraph(multiPdf=pdf)
