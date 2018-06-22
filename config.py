from pymongo import MongoClient
import json


apiLocation = 'localhost:5000'

validPdfName = '^\w+\.pdf$'

with open(chartStructure) as file:
    structure = json.load(file)
