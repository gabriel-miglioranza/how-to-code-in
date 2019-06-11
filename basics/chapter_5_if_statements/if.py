# This code contains simple examples about the use of if statements in Python.

# IF STATEMENTS

# A Simple Example:

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw'
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
print(1.0 = 1) # 1.0 is equal to 1?
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

