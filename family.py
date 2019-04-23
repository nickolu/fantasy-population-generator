from data_mappers.family_data_mapper import FamilyDataMapper

class Family(object):
    def __init__(self, name, members, social_status, relationships):
        self.name = name
        self.members = members
        self.social_status = social_status
        self.relationships = relationships

    @staticmethod
    def get_family(individual):
        family_data_mapper = FamilyDataMapper('family')
        return family_data_mapper.find_by_individual(individual)