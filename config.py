from pymongo import MongoClient

mongoURI = 'localhost'
mongoPort = 27017
collectionName = 'QE_Test_Data'
dbName = "QE_Database"
client = MongoClient(mongoURI, mongoPort)
db = client[dbName]
collection=db[collectionName]

validPdfName = '^\w+\.pdf$'

chartStructure = 'charts.json'

with open(chartStructure) as file:
    structure = json.load(file)

def cardsRegex():
    reg = "^("
    for card in structure['cards']:
        reg += card + "|"
    reg = reg[:-1]
    reg = reg + ")$"
    return reg

def testsRegex():
    reg = "^("
    for test in structure['tests']:
        reg += test + "|"
    reg = reg[:-1]
    reg = reg + ")$"
    return reg

def subTestsRegex(test):
    reg = "^("
    for subTest in structure['tests'][test]:
        reg += subTest + "|"
    reg = reg[:-1]
    reg = reg + ")$"
    return reg

def typeRegex(test,subTest):
    reg = "^("
    for type in structure['tests'][test][subTest]:
        reg += type + "|"
    reg = reg[:-1]
    reg = reg + ")$"
    return reg

def labelsRegex(test, subTest, type):
    reg = "^("
    for label in structure['tests'][test][subTest][type]:
        reg += label + "|"
    reg = reg[:-1]
    reg = reg + ")$"
