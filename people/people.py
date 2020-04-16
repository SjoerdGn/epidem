import numpy as np

from initialhelp import generate_age

class Person:
    
    def __init__(self):
        
        # Generate age and sex
        self.sex = np.random.randint(0,2)
        self.age = generate_age(self.sex)
        
        # Generate location