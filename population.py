from individual import Individual
from relationship import Relationship

class PopulationGenerator(object):
    def make_seed_generation(count):
        seed_generation = Individual.create_randoms(count);

        return seed_generation

    def generate_population(self, count):
        ratio_of_seed_generation_to_total_population = .10
        seed_generation = self.make_seed_generation(count * ratio_of_seed_generation_to_total_population)

        Relationship.create_random_relationships(seed_generation)

