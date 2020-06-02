import random
from Simulation import Simulation
class Person(Simulation):
    def __init__(self):
        self.is_infected=False
        self.is_dead=False
        self.days_infected=0

    def infect(self,simulation):
        randomAffected=random.randint(0,100)

        if randomAffected < simulation.infection_probablity:
            self.is_infected=True

    def heal(self):
        """" if person is not affected or healed then
        the days count is zero"""
        self.is_infected=False
        self.days_infected =0

    def die(self):
        self.is_dead=True

    def update(self,simulation):
        if not self.is_dead:
            if not self.is_infected:
                self.days_infected +=1
                if random.randint(0,100)<simulation.mortality_rate:
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()

