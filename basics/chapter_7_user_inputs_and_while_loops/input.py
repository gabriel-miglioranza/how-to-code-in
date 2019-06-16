# This code contains simple examples about getting user input in Python.

# How the input() Fucntion Works
# The input() function pauses the program and waits for the user to enter some text.
message = input('Tell me something, and I will repeat it back to you: ')
# The input() function puts the text from the user in the variable 'message'.
print(message)

# Writing Clear Prompts
# Be cleat to the user about what you want.
name = input('Please enter your name: ')
print('Hello, ' +  name + '!')

# Using int() to Accept Numerical Input
# The input() function considers all user input as strings, if we want to accept some numerical value, the use of int() function is necessary.
age = input('How old are you?')
age = int(age)
print(age >= 18)

# The Modulo Operator
# The modulo operator returns the remainder from the division of two integer numbers.
number = input("Enter a number, I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + 'is even.')
else:
    print('\nThe number ' + str(number) + 'is odd.')

