from mongo_data_mapper import MongoDbDataMapper

class IndividualDataMapper(MongoDbDataMapper):
    def convert_individual_to_dict(self, individual):
        return individual._document

    def create_individual(self, individual):
        self.collection.insert_one(individual._document)

        return individual

    # def create_individuals(self, individuals):
    #     individuals = map(lambda individual: self.convert_individual_to_dict(individual), individuals)

    #     self.collection.insert_many([individuals])

    def get_by_name(self, first_name="", last_name=""):
        return self.collection.find({'$and': [{'first_name':first_name}, {'last_name':last_name}]})

