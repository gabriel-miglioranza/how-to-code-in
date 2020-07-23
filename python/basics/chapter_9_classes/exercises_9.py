# Chapter 9 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# 9-1. Restaurant 
class Restaurant():
    '''Simple restaurant model.'''
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Simple statements that descibe the restaurant.'''
        print(self.restaurant_name.title() + ' offers ' + self.cuisine_type + ' food.')
    
    def open_restaurant(self):
        '''Simulate a restaurant oppening.'''
        print(self.restaurant_name.title() + ' is open.')
    
    def set_number_served(self, customers):
        '''Set the number of customers already served.'''
        self.number_served = customers

    def increment_number_served(self, customers):
        '''Increment the number of served customers.'''
        self.number_served += customers

restaurant = Restaurant('bistro chez remi', 'french')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
rest_1 = Restaurant('lancheria do parque', 'brazilian')
rest_2 = Restaurant('sukiyabashi jiro', 'japanese')
rest_3 = Restaurant("McDonald's", 'north american')

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()

# 9-3. Users
class User():
    def __init__(self, first_name, last_name, age, middle_name=''):
        '''Inititalize user attributes.'''
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def full_name(self):
        """Return the user's full name."""
        if self.middle_name != '':
            full_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            full_name = self.first_name + ' ' + self.last_name
        return full_name

    def describe_user(self):
        '''Print a statement about the user.'''
        print(self.full_name().title() + ' is ' + str(self.age) + ' years old.')

    def greet_user(self):
        '''Print a welcome message to the user.'''
        print('Welcome ' + self.full_name().title() + '!')    

    def increment_login_attempts(self):
        '''Increment the login attempts value by 1.'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Set the number of login attempts to zero.'''
        self.login_attempts = 0

user = User(first_name='antônio', middle_name='o cão', last_name='montanha' ,age=4)

user.describe_user()
user.greet_user()

# 9-4. Number Served
print(restaurant.number_served)
restaurant.set_number_served(12)
print(restaurant.number_served)

print(restaurant.number_served)
restaurant.increment_number_served(4)
print(restaurant.number_served)

# 9-5. Login Attempts
print(user.login_attempts)
for i in range(3): user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

# 9-6. Ice Cream Stand
class IceCreamStand(Restaurant):
    '''Represent aspects of restaurant, specific to ice cream stands.'''
    def __init__(self, restaurant_name, cuisine_type, flavors):
        '''
        Initialize attributes of parent class.
        Then initialize attributes specific to ice cream stands.
        '''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        '''Display the available flavors from the ice cream stand.'''
        print('The available flavors are: ')
        for flavor in self.flavors:
            print('- ' + flavor)

stand = IceCreamStand('IceCream', 'Italian', ['vanilla', 'chocolate', 'strawberry'])
stand.display_flavors()

# 9-7. Admin
# 9-8. Privileges

class Privileges():
    """Class of administrator's privileges."""
    def __init__(self):
        '''Initialize privileges attributess.'''
        self.privileges_list = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        '''Display all the administrator's privileges.'''
        print('The administrator has the following special privileges:')
        for privilege in self.privileges_list:
            print('- ' + privilege)

class Admin(User):
    '''
    Specify the special attributes given to the administrator user.
    Inherits the User class.
    '''
    def __init__(self, first_name, last_name, age, middle_name=''):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to ice cream stands.
        '''
        super().__init__(first_name, last_name, age, middle_name)
        self.privileges = Privileges()



admin = Admin('Chiara', 'Maria', 6)
admin.privileges.show_privileges()

# 9-9. Battery Upgrade
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
    
    def upgrade_battery(self):
        '''Upgrade the eletric car battery.'''
        if self.battery_size < 85:
            self.battery_size = 85 


class ElectricCar(Car):
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

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# 9-10. Imported Restaurant
# 9-11. Imported Admin
# 9-12. Imported Modules
# 9-13. OrderedDict Rewrite
# 9-14. Dice
# 9-15. Python Module of the Week
