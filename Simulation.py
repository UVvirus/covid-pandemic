import math
class Simulation():
    def __init__(self):
        self.day_number=1
        self.population_size=int(input("Enter the population:"))
        self.infection_percent=(int(input("Initial population affected:"))/100)
        self.infection_probablity=int(input("probablity of infection:"))
        self.infection_duration=int(input("Duration of  infection:"))
        self. mortality_rate=int(input("MOrtality rate:"))
        self. sim_days=int(input("No.of days for simulation:"))

    """""
        # Convert users population size to nearest perfect square for visual purposes
        self.root= math.sqrt(self.population_size) #For example, if population_size is 79, root = 8.8881
        # User did not enter a perfect square for the population
        if int(self.root + .5)**2 != self.population_size: # int(8.881 +.5)**2 =int(9.3881)**2 = 9**2 = 81 != 79
            self.root = round(self.root,0) # round(8.881, 0) = 9.0
            self.grid_size = int(self.root) #grid_size = 9
            self.population_size =self.grid_size**2 #population_size = 9*9 = 81
#the closest PERFECT SQUARE TO 79
            print("Rounding population size to " + str(self.population_size) + " for visual purposes.")
        # The user did enter a perfect square for the population
        else:
             self.grid_size = int(math.sqrt(self.population_size))

        print("percentage of population initially infected:")
        starting_infection_size = int(input("Enter the starting infection size:"))
        infection_percent = starting_infection_size/100
        print("probablity of a person will get infected if they contact with disease:")
        infection_probablity=int(input("Enter the infection probablity:"))
        print("how long the infection will last:")
        infection_duration=int(input("Enter the infection duration:"))
        print("mortality rate of those infected")
    """""