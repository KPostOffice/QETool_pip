from pymongo import MongoClient
import json


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
