
import unittest

from random_individual_traits import *

class TestRandomIndividualTraits(unittest.TestCase):
    def test_get_random_gender(self):
        gender = RandomIndividualTraits.get_random_gender()
        
        
        
        self.assertEqual(type(gender), unicode)


   
