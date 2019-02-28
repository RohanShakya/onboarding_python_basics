from pymongo import MongoClient


class Person:

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['testdb']
        self.collection = self.db['person_col']

    def create(self, person_doc):
        self.collection.insert_one(person_doc)

    def create_many(self, person_doc):
        self.collection.insert_many(person_doc)

    def retrieve(self):
        for x in self.collection.find():
            print(x)

    def update(self, condition, newvalues):
        self.collection.update_one(condition, {"$set": newvalues})

    def delete(self, conditiom):
        self.collection.delete_one(conditiom)


if __name__ == '__main__':
    p1 = Person()
    # p1.create({'name': 'saajan', 'phone': 55583883})

    p1.create_many([
        {'name': 'rohan', 'phone': 983776377},
        {'name': 'anil', 'phone': 66654664, 'address': 'yetkha baha'}
    ])

    #p1.update({"name": "rohan"}, {"name": "anil"})

    #p1.delete({"name": "anil"})

    p1.retrieve()
