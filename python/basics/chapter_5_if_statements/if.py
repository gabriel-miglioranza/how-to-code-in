# This code contains simple examples about the use of if statements in Python.

# IF STATEMENTS

# A Simple Example:

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        # if the item is equal to 'bmw' Python runs the next line 
        print(car.upper())
    else:
        print(car.title())

# Conditional Tests

# Checking for Equality

car = 'bmw' # assign 'bmw' to variable car
print(car == 'bmw') # True or False? The variable car is equal to 'bmw'. 
print(car == 'audi') # True or False? The variable car is equal to 'audi'.

# Ignoring Case When Checking for Equality

# The conditional test for strings is case sensitive.
car = 'audi' # assign 'audi' to variable car
print(car == 'Audi') # True or False? The variable car is equal to 'Audi'. 
print(car == 'audi') # True or False? The variable car is equal to 'audi'.

# Checking for Inequality

requested_topping = 'mushrooms'
# The next line test if requested_topping is not equal to 'anchovies'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# Numerical Comparisons

age = 18
print(age == 17) # age is equal to 17?
print(age == 18) # age is equal to 18?
print(1.0 == 1) # 1.0 is equal to 1?
print(age < 21) # age is less than 21?
print(age <= 21) # age is less than or equal to 21?
print(age > 21) # age is greater than 21?
print(age >= 21) # age is greater than or equal to 21?


answer = 17

if answer != 42: 
    print('That is not the correct answer. Please try again!')

# Checking Multiple Conditions 

# Using 'and' to Check Multiple Conditions
# In this statement both conditions must be satisfied to Python return a True value.

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# Using 'or' to Check Multiple Conditions 
# In this statement only one conditions must be satisfied to Python return a True value.

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_1 = 22
print(age_0 >= 21 or age_1 >= 21)

# Checking Whether a value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pinapple']
print('mushrooms' in requested_toppings) # Is 'mushrooms' in requested_toppings?
print('pepperoni' in requested_toppings) # Is 'pepperoni' in requested_toppings?

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')

# Boolean Expressions 
# In Python is possible to store a boolean in a variable.
game_active = True 
can_edit = False

# if Statements

# Simple if Statements
# if conditional_test:
#   do something
age = 19
conditional_test = age >= 16
if conditional_test:
    print('You are old enough to vote!')

# if-else Statements
# if-else statements are used when you want to execute a set of actions when the conditional test fails (returns False).

age = 19
conditional_test = age >= 16
if conditional_test:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else: 
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 16!')

# The if-elif-else Chain

# The if-elif-chain can be understood through the following example:
# You are going to the movies and decided to buy the ticket from the movie theater's website. The price for a adult is the full price, let it be $18, but if you have less than 18 years you pay only half of the price, and if you have less than 8 years you get it for free. How you print the correct price depending on the user age? Like this:

age = 12

if age <= 8:
    print('This ticket is free, have fun with the movie!')
elif age < 18:
    print('The ticket costs $9.')
else: 
    print('The ticket costs $18.')

# Using Multiple elif Blocks 
# Suppose now that the movie theater wants to reach the elderly market, as a incentive they put the ticket's price $13 for people over 65 years. With a simple alteration of the above code we can print the correct message for those who have more than 65 years.

if age <= 8:
    print('This ticket is free, have fun with the movie!')
elif age < 18:
    print('The ticket costs $9.')
elif age > 65:
    print('The ticket costs $13.')
else: 
    print('The ticket costs $18.')

# Ommiting the else Block
# Python does not require the else block at the end of an if-elif chain.

if age <= 8:
    print('This ticket is free, have fun with the movie!')
elif age < 18:
    print('The ticket costs $9.')
elif age > 65:
    print('The ticket costs $13.')
elif age >= 18 and age <= 65: 
    print('The ticket costs $18.')

# The else block is also known as the default in the if-elif chain, because if the previous conditions in a if-elif are not satified Python runs the else block. 

# Testing Multiple Conditions
# The if-elif-else chain permits only one test to pass, if you want to check all the conditions of interest you need test one by one separately.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

# Using if Statements with Lists

# Checking for Special Items
# Put a if statement inside a for loop to check for a special item in a list.
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else: 
        print('Adding' + requested_topping + '.')

print('\nFinished making your pizza!')

# Checking That a List Is Not Empty
requested_toppings = []
# The following line checks if requested_toppings is empty.
if requested_toppings: 
    for requested_topping in requested_toppings: 
        print('Adding' + requested_topping + '.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    # The next line checks if the item (requested_topping) from the list
    # (requested_toppings) is in the list (available_toppings).
    if requested_topping in available_toppings:
        print('Adding'+ requested_topping + '.')
    else: 
        print("Sorry, we don't have " + requested_topping + ".")

print('\nFinished making your pizza!')

