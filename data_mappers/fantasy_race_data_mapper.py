from mongo_data_mapper import MongoDbDataMapper

class FantasyRaceDataMapper(MongoDbDataMapper):
    def get_by_name(self, name):
        results = self.collection.find({'name': name.title()})

        return [i for i in results]
