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

