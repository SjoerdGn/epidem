import numpy as np

#from initialhelp import generate_age
from epidem.people.initialhelp import generate_age
from epidem.locations.location import Location
import datetime as dt
from epidem.people.infectiousness  import logarit

class Person:
    
    def __init__(self, width, height, clock, formula = logarit):
        
        # Generate age and sex
        self.sex = np.random.randint(0,2)
        self.age = generate_age(self.sex)
        self.infected = False
        self.ill = False
        self.infected_date_time = None
        self.ill_date_time = None
        #self.infect_len = dt.timedelta(days = 0)
        #self.ill_len = dt.timedelta(days = 0)
        self.deceased = False
        self.infectable = formula(self.age)
        self.infectious = False
        
        # Generate location
        self.location = Location(width, height)
        self.location.generate_location_basic()
        
        # Use clock
        self.clock = clock
      
    def touch(self):
        var = np.random.rand(1)
        if var < self.infectable:
            self.infect()
        
        
    def infect(self):
        self.infected = True
        self.infected_date_time = self.clock.date_time
        
        
    def check_ill(self, ill_time = dt.timedelta(days = 5)):
        if self.infected_date_time is not None:
            if ill_time <= (self.clock.date_time - self.infected_date_time):
                self.make_ill()
        # Only basic yet
        
        
    def make_ill(self):
        self.ill = True
        self.ill_date_time = self.clock.date_time
        
    def check_infectious(self, infectious_time = dt.timedelta(days = 5)):
        if self.infected_date_time is not None:
            if infectious_time <= (self.clock.date_time - self.infected_date_time):
                    self.infectious = True
        
        # Only basic yet