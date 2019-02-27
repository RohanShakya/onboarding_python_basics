from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']
collection = db['testcol1']

for x in collection.find({"name": "roshni"}, {"_id":0}):
    print(x)

