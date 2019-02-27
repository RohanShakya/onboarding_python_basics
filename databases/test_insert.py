from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']
collection = db['testcol1']

person = {
    'name': 'anil',
    'address': 'yettkha bahal',
    'phone_no': 2226635
}

result = collection.insert_one(person)

print(result.inserted_id)