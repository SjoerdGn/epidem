import numpy as np

#from initialhelp import generate_age
from epidem.people.initialhelp import generate_age
from epidem.locations.location import Location

class Person:
    
    def __init__(self, width, height):
        
        # Generate age and sex
        self.sex = np.random.randint(0,2)
        self.age = generate_age(self.sex)
        self.infected = False
        self.ill = False
        self.infect_len = 0
        self.ill_len = 0
        
        # Generate location
        self.location = Location(width, height)
        self.location.generate_location_basic()