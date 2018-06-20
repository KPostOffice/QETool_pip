from pymongo import MongoClient

mongoURI = 'localhost'
mongoPort = 27017
collectionName = 'QE_Test_Data'
dbName = "QE_Database"
client = MongoClient(mongoURI, mongoPort)
db = client[dbName]
collection=db[collectionName]
