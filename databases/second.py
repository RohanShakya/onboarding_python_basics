import pandas as pd
from first import Person


class CsvParser:
    def __init__(self):
        self.person1 = Person()
        self.person1.collection = self.person1.db['sample_col']

    def insert_into_db(self):
        dataframe = pd.read_csv('D:\python_onboarding\sample_csv.csv')
        # print(dataframe)
        mydict = dataframe.to_dict(orient='records')

        self.person1.create_many(mydict)

    def retrieve(self):
        for x in self.person1.collection.find():
            print(x)


if __name__ == '__main__':
    csvparser = CsvParser()
    csvparser.insert_into_db()
    csvparser.retrieve()


