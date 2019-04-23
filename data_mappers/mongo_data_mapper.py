from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['PopulationGenerator']

class MongoDbDataMapper(object):
    def __init__(self, collection_name):
        self.collection = db[collection_name]
  
    def get_by_id(self, id):
        return self.collection.find_one({'_id':id})
    
    def get_one(self):
        return self.collection.find_one()
    
    def get_all(self):
        results = self.collection.find({})
        
        return [i for i in results]

    def get_by_name(self, name):
        results = self.collection.find({'name': name})

        return [i for i in results]

