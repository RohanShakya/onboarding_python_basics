from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']
collection = db['testcol1']

condition = {"name": "sabin"}

collection.delete_many(condition)

for x in collection.find():
    print(x)
