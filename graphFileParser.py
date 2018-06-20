class multiGraph():
    def __init__(fileName):
        self.fileName = fileName
        self.pdf = ""
        self.graphs = []

    def construct(self):
        pdf = ""
        graphs = []   # new empty non-instance variables allow for nonassignment if input is invalid
        options = []
        file_ob = open(self.fileName, "r")
