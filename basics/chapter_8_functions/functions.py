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
describe_pet('chaira', 'cat')