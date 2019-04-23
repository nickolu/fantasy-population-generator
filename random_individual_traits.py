import random
import json
from numpy.random import choice
from data_mappers.individual_data_mapper import IndividualDataMapper
from data_mappers.fantasy_race_data_mapper import FantasyRaceDataMapper


YOUNGEST_MARRIAGE_ALLOWED = 16

class RandomIndividualTraits(object):
    @staticmethod
    def get_random_fantasy_race():
        fantasy_race_data_mapper = FantasyRaceDataMapper('fantasy_races')
        fantasy_races = fantasy_race_data_mapper.get_all()
        
        return choice(fantasy_races)
    
    @staticmethod
    def get_random_age_by_fantasy_race_lifespan(race):
        fantasy_race_data_mapper = FantasyRaceDataMapper('fantasy_races')
        fantasy_race = fantasy_race_data_mapper.get_by_name(race)
        
        if fantasy_race:
            lifespan = fantasy_race[0]['lifespan']
        else:
            lifespan = 100

        age_choices = [i for i in range(lifespan)]

        return choice(age_choices)
    
    @staticmethod
    def get_random_first_name(names_table=None):
        random_name = ""

        if not names_table:
            names_table = "nonbinary_names"

        with open('./json-data/names.json') as names_json:
            names = json.load(names_json)[names_table]
            random_name = choice(names)
        
        return random_name
    
    @staticmethod
    def get_random_last_name():
        return RandomIndividualTraits.get_random_first_name()
    
    @staticmethod
    def get_random_full_name(names_table=None):
        return "{} {}".format(get_random_first_name(), get_random_last_name())
    
    @staticmethod
    def get_random_gender():
        genders = ['male', 'female', 'ambiguous']

        return choice(genders, p=[0.45,0.45,0.1])

    @staticmethod
    def get_random_marriage_length(individual_a_age, individual_b_age):
        max_years_married = max([individual_a_age, individual_b_age]) - YOUNGEST_MARRIAGE_ALLOWED
        
        return choice(range(max_years_married))
