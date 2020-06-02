from Simulation import Simulation
from Person import Person
import random
class Population():
    def __init__(self,simulation):
        self.population=[]
        for i in range(simulation.population_size):
            person=Person()
            self.population.append(person)

    def initial_infection(self,simulation):
        infected_count=int(round(simulation.infection_percent *  simulation.population_size,0))
        for i in range(infected_count):
          self.population[i].is_infected=True
          self.population[i].days_infected=1

        random.shuffle(self.population)

    def spread_infecton(self,simulation):
        for i in range(len(self.population)):
            # ith person is ALIVE, see if they should be infected.
            # Don't bother infecting a dead person, they are infected and dead.
            # Check to see if adjacent Persons are infected
            if self.population[i].is_dead == False:
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                    elif i < len(self.population)-1:
                        #These Person objects  are in the middle of the list
                       if self.population[i+1].is_infected or self.population[i-1].is_infected:
                            self.population[i].infect(simulation)
                    elif i == len(self.population)-1:
                        if self.population[i -1 ].is_infected:
                            self.population[i].infect(simulation)

    def update(self,simulation):
        simulation.day_number += 1
        for person in self.population:
            person.update(simulation)

    def display_statistics(self,simulation):
        total_infected_count= 0
        total_death_count=0
        #Looping through the whole population
        for person in self.population:
            if person.is_infected:
                total_infected_count +=1
                if person.is_dead:
                    total_death_count +=1
        infected_percent = round( 100*(total_infected_count/simulation.population_size) ,4)
        death_percent = round(100*(total_death_count/simulation.population_size),4)
        print("\n-----Day # " + str(simulation.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected_count) + " / " +
              str(simulation.population_size))
        print("Total Deaths: " + str(total_death_count) + " / " +
              str(simulation.population_size))

    def grapics(self):
        status=[]

        for person in self.population:
            if person.is_dead:
                char='X'
            else:
                if person.is_infected:
                    char='I'
                else:
                    char='O'
            status.append(char)

        for letter in status:
            print(letter,end='-')

#objects creation
sim = Simulation()
pop = Population(sim)
#setting initial conditions
pop.initial_infection(sim)
pop.display_statistics(sim)
pop.grapics()
input("press enter to begin:")

for i in range(1,sim.sim_days):
    # For a single day, spread the infection, update the population, display
    #statistics and graphics
    pop.spread_infecton(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    pop.grapics()
    # If it is not the last day of the simulation, pause the program
    if i != sim.sim_days - 1:
        input("\nPress enter to advance to the next day.")

