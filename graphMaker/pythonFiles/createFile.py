import readline
import pythonFiles.apiRequest as apiRequest
import re
import argparse

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=False,
            help='Output txt file, out.txt by default', default="out.txt")
    
    req = apiRequest.QEdataRequest()
    
    print("This tool is for creating txt files which are of proper form so that they" \
            "can be called with xeqt.py, which makes a PDF booklet. Use tab for autocomplete")
    
    def writeLine():
        ###########################################################################
        validCards = req.validCards()
        completer = MyCompleter(validCards + ["next"])
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
    
        cards = []
        while(True):
            userIn = input("Enter desired card ('next' to continue): ")
            if(userIn == "next"):
                if(not cards):
                    raise IOError("No input for card")
                break
            if(not userIn in validCards):
                raise IOError("Invalid card name")
            cards.append(userIn)
        ###########################################################################
    
        validTests = req.validTests()
        completer = MyCompleter(validTests)
        readline.set_completer(completer.complete)
    
        test = input("Enter test name: ")
        if(not test in validTests):
            raise IOError("Invalid test name")
        ###########################################################################
    
        validSubtests = req.validSubtests(test)
        completer = MyCompleter(validSubtests)
        readline.set_completer(completer.complete)
    
        subtest = input("Enter subtest name: ")
        if(not subtest in validSubtests):
            raise IOError("Invalid subtest name")
        ###########################################################################
    
        validTypes = req.validTypes(test, subtest)
        completer = MyCompleter(validTypes)
        readline.set_completer(completer.complete)
    
        type = input("Enter type: ")
        if(not type in validTypes):
            raise IOError("Invalid type")
        ###########################################################################
    
        validLabels = req.validLabels(test, subtest, type)
        completer = MyCompleter(validLabels)
        readline.set_completer(completer.complete)
    
        labels = []
        while(True):
            userIn = input("Enter desired label ('next' to continue): ")
            if(userIn == "next"):
                if(not labels):
                    raise IOError("No input for label")
                break
            if(not userIn in validLabels):
                raise IOError("Invalid label")
            labels.append(userIn)
        ###########################################################################
    
        completer = MyCompleter([])
        readline.set_completer(completer.complete)
        start = input("Enter start date of the form YYYY-MM-DD: ")
        end = input("Enter end date of the form YYYY-MM-DD: ")
    
        array = [",".join(cards),test,subtest,type,",".join(labels),start,end]
        return ":".join(array)+"\n"
    
    def createFile():
    
        pdfName = input("Enter the name of the PDF which you want to create: ")
        if(pdfName == ""):
            raise IOError("No name provided")
    
        if(not re.match(r'^.+\.pdf$', pdfName)):
            pdfName += ".pdf"
    
        toWrite = pdfName + "\n"
    
        toWrite = toWrite + writeLine()
    
        while(True):
            userIn = input("Would you like to make another page (y/n)?")
            if(userIn.lower() == "n" or userIn.lower() == "no"):
                break
            elif(userIn.lower() != "y" and userIn.lower() != "yes"):
                print("Input not recognized")
                continue
    
            toWrite = toWrite + writeLine()
    
        fo = open(parser.parse_args().output, "w")
        fo.write(toWrite)
        fo.close()
    
    createFile()

if __name__ ==  '__main__':
    main()
