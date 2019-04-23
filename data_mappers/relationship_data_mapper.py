from mongo_data_mapper import MongoDbDataMapper

class RelationshipDataMapper(MongoDbDataMapper):

    def find_relationships_for_individual(self, individual):
        
        return self.collection.find({"$or" : [{'partner_a': individual}, {'partner_b': individual}]})

    def create_relationship(self, partner_a, partner_b, status, duration):
        self.collection.insert_one({"partner_a": partner_a.__dict__, "partner_b": partner_b.__dict__, "status":status, "duration": duration})
