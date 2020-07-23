# This code contains simple examples about working with classes in Python.

# Object-oriented programming you write classes that represent real-world things and situations, and create objects based on this classes.

# Creating and Using a Class

# Creating the Dog Class
# You can model almost anything using classes. This is an example of a class named Dog. Every dog object of the class Dog has a name, age and can sit and roll over by command.
class Dog():
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(self.name.title() + ' rolled over!')

# The __init__() Method
# A function that's a part of a class is a method. The __init__() method is  a special method in python (as every __ method is). The __init__() method is called every time a new instance of the Class is created, it receives as defaul paramenter the instance itself (self). 

# Making an Instance from a Class
# Suppose you want to create a Dog named Willie that is 6 years old. This is how you do it with OOP.
my_dog = Dog('willie', 6)

# Accessing Attributes
# To print Willie's name and age we need to get the attributes from the object my_dog like this.
print("My dog's name is " + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')

# Calling Methods
# The Dog Class has two inner methods besides the __init__() method. The sit() and roll_over() methods can be called by an istance.
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
# Now we are going to create a new Dog with different attributes.
your_dog = Dog('lucy', 3)
print("My dog's name is " + your_dog.name.title() + '.')
print('My dog is ' + str(your_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()

# Working with Classes and Instances

# The Car Classes
class Car():
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize the attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_level = 100

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's milleage.'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles

    def fill_gas_tank(self):
        self.fuel_level = 100
    

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute
# If you put a default value for an attribute when you instantiate the Class you doesn't need to pass a value for that attribute necessarily.
my_new_car.read_odometer()

# Modifying Attribute's Value Directly
# The simplest way to change a value is by direct access.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
# Updating the value using a Class method.
my_new_car.update_odometer(24)
my_new_car.update_odometer(20)

# Increment an Attribute's Value Through a Method
# Use the method increment_odometer() to just increment the odometer value.
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.read_odometer()

# Inheritance
# If you want to write a specialized class from another already existant class you can use inheritance. The original class is called parent class, and the derivated one is the child class. 

# The __init__() Method for a Child Class
# We are going to create a new class named EletricCar from the parent class Car. Just use the following syntax.

# The super() function is a special one. Its necessary to make the connection between the parent class (superclass) and the child one (subclass).

class ElectricCar(Car):
    '''Represents aspects of car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def fill_gas_tank(self):
        """Eletric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# Defining Attributes and Mehods for the Child Class
# In the child class you can create attributes and methods apart from the parent class. 
my_tesla.describe_battery()

# Overriding Methods from the Parent Class
# You can override existent methods from the parent class in the child class.
my_tesla.fill_gas_tank()

# Instances as Attributes
# In the next example let's create a new class named Battery to descibe the battery inside the EletricCar2 class.
class Battery():
    '''A simple attempt to model a battery for an electric car.'''
    
    def __init__(self, battery_size=70):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
    
    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 70:
            battery_range = 240
        elif self.battery_size == 85:
            battery_range = 270
        
        message = 'This car can go approximately ' + str(battery_range)
        message += ' miles on a full charge.'
        print(message) 

class EletricCar2(Car):
    '''Represents aspects of car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Eletric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = EletricCar2('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Modeling Real-World Objects
