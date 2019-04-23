import json
import random
from family import Family
from data_mappers.fantasy_race_data_mapper import FantasyRaceDataMapper
from data_mappers.relationship_data_mapper import RelationshipDataMapper
from numpy.random import choice

CHANCE_OF_MARRIAGE = 0.1

relationship_data_mapper = RelationshipDataMapper('relationships')

def duration_string(duration):
    if duration:
        if duration == 1:
            return "for {} year".format(duration)
        if duration > 1:
            return "for {} years".format(duration)
    
    return ""

class Relationship():
    def __init__(self, individual_a, individual_b, status, duration=None):
        self.individual_a = individual_a
        self.individual_b = individual_b
        self.status = status
        self.duration = duration

    def announce(self):
        individual_a = self.individual_a
        individual_b = self.individual_b
        

        print "{} {} and {} {} have are {}".format(individual_a.first_name, 
                                                   individual_a.last_name, 
                                                   individual_b.first_name, 
                                                   individual_b.last_name,
                                                   self.status)

    @staticmethod
    def create_new(individual_a, individual_b, status, duration=None):
        relationship = Relationship(individual_a, individual_b, status, duration)
        relationship_data_mapper.create_relationship(individual_a, individual_b, status, duration)

        return relationship

    @staticmethod
    def create_random_relationship(individual_a, individual_b, romantic_or_platonic, duration=None):
        relationship_status = Relationship.get_random_relationship_status(romantic_or_platonic)
        relationship = Relationship(individual_a, individual_b, relationship_status, duration);

        return relationship

    @staticmethod
    def create_random_platonic_relationship(individual_a, individual_b, duration=None):
        platonic_relationship = Relationship.create_random_relationship(individual_a, individual_b, "platonic", duration)

        return platonic_relationship

    @staticmethod
    def create_random_romantic_relationship():
        romantic_relationship =Relationship.create_random_relationship(individual_a, individual_b, "romantic", duration)

        return romantic_relationship

    @staticmethod
    def create_marriage(individual_a, individual_b, duration=None):
        marriage = Relationship(individual_a, individual_b, "married", duration)

        return marriage

    @staticmethod
    def set_random_relationships_for_population(population):
        for individual_a in population:
            for individual_b in population:
                randomly_create_marriage(individual_a, individual_b)
    
    @staticmethod
    def get_random_relationship_status(romantic_or_platonic=None):
        random_relationship_status = ""

        if not romantic_or_platonic:
            romantic_or_platonic = "platonic"

        with open('./json-data/relationship-statuses.json') as relationship_statuses_json:
            statuses = json.load(relationship_statuses_json)[romantic_or_platonic]
            random_relationship_status = random.choice(statuses)
        
        return random_relationship_status

    @staticmethod
    def are_romantically_compatible(individual_a, individual_b):
        fantasy_race_data_mapper = FantasyRaceDataMapper('fantasy_races')
        

        individual_a_can_mate_with = fantasy_race_data_mapper.get_by_name(individual_a.fantasy_race_name)[0]['can_mate_with']
        individual_b_can_mate_with = fantasy_race_data_mapper.get_by_name(individual_b.fantasy_race_name)[0]['can_mate_with']

        if individual_a.age < 16 or individual_b.age < 16:
            print "can't marry since one of them is underage"
            return False
        
        if individual_a.fantasy_race_name.title() not in individual_b_can_mate_with:
            print "individual_a unable to mate with individual_b"
            return False

        if individual_b.fantasy_race_name.title() not in individual_a_can_mate_with:
            print "individual_b unable to mate with individual_a"
            return False
        
        if individual_a == individual_b:
            print "one cannot marry oneself"
            return False
        
        family_a = Family.get_family(individual_a)
        family_b = Family.get_family(individual_b)
        
        if family_a and family_b: 
            if individual_b in family_a.members:
                print "the two are family members"
                return False
            
            if individual_a in family_b.members:
                print "the two are family members"
                return False

        return True


    @staticmethod
    def randomly_decide_if_two_individuals_are_married(individual_a, individual_b, duration=None, chance_of_marriage = CHANCE_OF_MARRIAGE):
        set_married = False

        if Relationship.are_romantically_compatible(individual_a, individual_b):
            set_married = choice([True, False],p=[chance_of_marriage, 1-chance_of_marriage])
        
        if not duration:
            duration = choice(range(min(individual_a.age, individual_b.age)))
        
        if set_married:
            Relationship.create_marriage(individual_a, individual_b)

        return set_married
                    


    