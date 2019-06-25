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
 