# This code contains simple examples about importing classes in Python.
# Importing a single class
from classes import Car

# Importing Multiple Classes in a Module
from classes import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# Importing All Classes from a Module
# from classes import *

# Import a Module into a Module