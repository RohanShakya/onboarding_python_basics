from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']
collection = db['testcol1']

condition = {"name": "anil"}
newvalues = {"$set": {"address": "Yetkha Baha", "phone_no": 9898989800}}

collection.update_one(condition, newvalues)

for x in collection.find():
    print(x)
