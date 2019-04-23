import random
from operator import attrgetter
from random_individual_traits import RandomIndividualTraits
from relationship import Relationship
from base import BaseEntity
from data_mappers.individual_data_mapper import IndividualDataMapper

individual_data_mapper = IndividualDataMapper('individuals')

class Individual(BaseEntity):

    field_mapping = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'profession': 'profession',
        'industry': 'industry',
        'social_status': 'social_status',
        'age': 'age',
        'district': 'district',
        'fantasy_race_name': 'fantasy_race_name',
        'gender': 'gender',
        'gender_preference': 'gender_preference',
        'family_id': 'family_id'
    }

    def __init__(self, 
                 document):
        BaseEntity.__init__(self, document)

        print "a",self.age,"year-old",self.fantasy_race_name,"named",self.first_name,self.last_name,"was just created!"

    @staticmethod
    def create_random():
        return create_random()

    @staticmethod
    def create_randoms(count):
        return create_randoms(count)

    @staticmethod
    def find_by_id(self):
        return individual_data_mapper.get_by_id({'_id'})

    @staticmethod
    def find_by_name(first_name, last_name):
        return individual_data_mapper.get_by_name(first_name=first_name, last_name=last_name)

    @staticmethod
    def create_new(**kwargs):
        
        individual = Individual(kwargs)
        individual_data_mapper.create_individual(individual)

        return individual

    @staticmethod
    def create_random():
        random_fantasy_race = RandomIndividualTraits.get_random_fantasy_race()

        individual = Individual.create_new(
            first_name=RandomIndividualTraits.get_random_first_name(), 
            last_name=RandomIndividualTraits.get_random_last_name(),
            fantasy_race_name=random_fantasy_race['name'],
            age=RandomIndividualTraits.get_random_age_by_fantasy_race_lifespan(random_fantasy_race['name']),
            gender=RandomIndividualTraits.get_random_gender())

        return individual

    @staticmethod
    def create_randoms(count):
        individuals = [Individual.create_random() for i in range(count)]

        return individuals

    @staticmethod
    def find_one():
        return individual_data_mapper.get_one()

    @staticmethod
    def get_highest_attribute_among_individuals(individuals, attribute):
        return max(individuals, key=attrgetter(attribute))
    
    @staticmethod
    def get_lowest_attribute_among_individuals(individuals, attribute):
        return min(individuals, key=attrgetter(attribute))

    def greet(self):
        return "Hi, my name is {} {}.".format(self.first_name, self.last_name)

    def list_traits(self):
        for trait_name, trait in self.__dict__.iteritems():
            print trait_name, trait

    def get_attribute(self, attribute=None):
        return getattr(self, attribute)
    
    