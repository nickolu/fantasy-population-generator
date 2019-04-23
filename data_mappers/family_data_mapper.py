from mongo_data_mapper import MongoDbDataMapper

class FamilyDataMapper(MongoDbDataMapper):
    def find_by_individual(self, individual):
        _id = individual.family_id or ""

        return self.collection.find_one({'_id': _id})
