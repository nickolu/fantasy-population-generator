
import unittest

from relationship import Relationship
from data_mappers.relationship_data_mapper import RelationshipDataMapper
from individual import Individual

relationship_data_mapper = RelationshipDataMapper('relationships')

class TestRelationship(unittest.TestCase):

    def test_are_romantically_compatible(self):
        jon = Individual.create_new(first_name='Jon', 
                 last_name='Snow', 
                 profession='King', 
                 industry='Government',
                 social_status='Noble',
                 age=30,
                 district='Winterfell',
                 description='A nice man',
                 fantasy_race_name='human',
                 gender='male',
                 gender_preference='female',
                 family_id='stark')

        dany = Individual.create_new(first_name='Dany', 
                 last_name='Targaryan', 
                 profession='Queen', 
                 industry='Dragons',
                 social_status='Noble',
                 age=23,
                 district='Grasslands',
                 description='A white haired woman',
                 fantasy_race_name='human',
                 gender='female',
                 gender_preference='male',
                 family_id='targaryan')

        are_compatible = Relationship.randomly_decide_if_two_individuals_are_married(jon, dany, chance_of_marriage=1)


        self.assertEqual(are_compatible, True)

        print "ID", jon.id

        print relationship_data_mapper.find_relationships_for_individual(jon.id)[0]

    def test_get_random_relationship_status(self):
        print Relationship.get_random_relationship_status()

        
    def test_create_random_platonic_relationship(self):
        individual_a = Individual.create_random()
        individual_b = Individual.create_random()
        random_relationship = Relationship.create_random_platonic_relationship(individual_a, individual_b, 1)
        random_relationship.announce()


    def test_create_relationship(self):
        individual_a = Individual.create_random()
        individual_b = Individual.create_random()

        friendship = Relationship.create_new(individual_a, individual_b, "friends", 10)

        friendship.announce()

   
