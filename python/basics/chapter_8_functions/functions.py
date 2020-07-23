# This code contains simple examples about working with functions in Python.

# functions are blocks of code that are designed to do one specific job.
# When you need to perform a task multiple times throughout your program, you don't need to type all the code again. An example is the print() function.

# Defining a Function 
# This is a simple struture of a function:
def greet_user():
    # The text bellow is a docstring it describe what the function does.
    """Display a simple greeting."""
    print('Hello!')

greet_user()

# Passing Information to a Function
# Between the parentheses you can pass an argument to the function, this variable can than be used inside the function.
def greet_user(username):
    '''Display a simple greeting.'''
    print('Hello, ' + username.title() + '!')

greet_user('jesse')
greet_user('sarah')

# Arguments and Parameters

# Passing Arguments
# A function definition can have multiple arguments. You can pass arguments to functions in a number of ways.

# Positional Arguments
# One way of passing arguments is the 'positional arguments'. In this way when you are calling the function you need to match the position of the arguments with the position from the defined parameters.
def describe_pet(pet_name, animal_type):
    '''Display information about a pet.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('montanha', 'dog')

# Multiple Function Calls
describe_pet('chiara', 'cat')

# Order Matters in Postional Arguments
describe_pet('dog', 'montanha')

# Keyword Arguments
# With Keyword arguments you can change the order from the call and still get the desired result. 
describe_pet(animal_type='dog', pet_name='montanha')

# Default Values
# In Python you can set a default value to a parameter. The default value is used when its value is not overwritten in the function call.
def describe_pet(pet_name, animal_type='dog'):
    '''Display information about a pet.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('montanha')
describe_pet('chiara', 'cat')

# Equivalent Function Calls
# The following function calls have the same result.
# A dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument Errors
# If you forget to put an argument in the function call Python will return an error message.
#describe_pet()

# Return Values
# A function can return a value to be assigned to a variable.

# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Opition
# In the last example a person can have a middle name or it doesn't. 
# You can make a optional argument to circumvent this problem.
def get_formatted_name(first_name, last_name, middle_name=''):
    '''Return a full name, neatly formatted.'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dictionary
# A function can return any kind of value you need it to.

def build_person(first_name, last_name):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Using a Function with a while Loop

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')
print('Goodbye!')

# Passing a List
# It is often useful to pass an entire list to a function.
def greet_users(names):
    '''Print a simple greeting to each user in the list.'''
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

# Modifying a List in a Function
# Watchout! Any changes of a list inside a function is permanent.
def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    '''
    while unprinted_designs:
        current_design =  unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Show all the models that were printed.'''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# If you don't want to modify the original list during the function execution pass a copy of the list like this:
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

# Passing an Arbitrary Number of Arguments
# Sometimes you won't know ahead of time how many arguments a function needs to accept. In python you can use a especial type of argument conventionally named *args. Here is an example:
def make_pizza(*toppings):
    '''Summarize the pizza we are about to make.'''
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)
print('Pizza 1: ')
make_pizza('pepperoni')

print('Pizza 2: ')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
# If you want a function to accept different kinds of arguments you need to follow a specific order in the function definition. First, the positional arguments and then the arbitrary arguments.

def make_pizza(size, *toppings):
    '''Summarize the pizza we are about to make.'''
    print('\nMaking a '+ str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)
print('Pizza 1: ')
make_pizza(16, 'pepperoni')

print('Pizza 2: ')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
# If you need to pass an arbitrary number of arguements but you doesn't know ahead of time what kind of information will be passed to the function, use the **kwargs in the function definition.

def build_profile(first, last, **user_info):
    '''Build a dictionary containig everything we know about the user.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

# Storing Your Functions in Modules
# Storing function in modules is useful when you want to reuse functions.

# Importing an Entire Module
# We will import the entire module from 'module.py'.
#import sandwich
# Now the we can call the function make_sandwich().
#make_sandwich(15, 'bread', 'peanut butter', 'jelly')
# Non available Syntax!

# Importing Specific Functions 
# We will import just the function make_sandwich() from 'module.py'.
from sandwich import make_sandwich
# Now the we can call the function make_sandwich().
make_sandwich(15, 'bread', 'peanut butter', 'jelly')

# Using as to Give a Function an Alias
# We will import just the function make_sandwich() from 'module.py'.
from sandwich import make_sandwich as ms
# Now the we can call the function make_sandwich() as ms.
ms(15, 'bread', 'peanut butter', 'jelly')

# Using as to Give a Module an Alias
# We will import the 'module.py' as m.
import sandwich as s
# Now the we can call the function make_sandwich() as m.make_sandwich().
s.make_sandwich(15, 'bread', 'peanut butter', 'jelly')

# Importing All Functions in a Module
# We will import all functions from 'module.py'.
from module import *
# Now the we can call the function make_sandwich().
make_sandwich(15, 'bread', 'peanut butter', 'jelly')

# Styling Functions

