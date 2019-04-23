
import unittest
import numpy

from individual import Individual


class TestIndividualStaticMethods(unittest.TestCase):
    # def test_create_random(self):
    #     individual_a = Individual.create_random()
    #     individual_b = Individual.create_random()
    #     print individual_a.greet()
    #     print individual_b.greet()
    #     print individual_a.list_traits()


    #     self.assertEqual(type(str(individual_a.first_name)), str)

    def test_create_randoms(self):
        population = Individual.create_randoms(10)

        for individual in population:
            individual.greet()
