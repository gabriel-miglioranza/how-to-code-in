# This code contains simple examples about working with while loops in Python.

# The while Loop in Action
# The while loop executes an action until a certain statement is True. For example we can construct a while loop that counts from 1 to 5 like this:
current_number = 1
# You can read this statement like: "While current_number is less or equal to five execute the following code."
while current_number <= 5: 
    print(current_number)
    # The '+= 1' sign adds 1 to the current_number value.
    current_number += 1

# Letting the User Choose When to Quit 
prompt = '\nTell me something, and I will repeat it back to you: '
promt += "\nEnter 'quit' to end the program."
# In this case the while loop just breaks its execution when the user enters 'quit' in the prompt.
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

# Using Flag
# A flag is a variable that holds a boolean value (True or False), its used to determine when a while loop should end.

active = True

while active;
    message = input(prompt)

    if message == 'quit':
        active = False
    else: 
        print(message)
    
# Using break to Exit a Loop
# To exit a while loop immediately use the command break. It can also be used in for loops.

prompt = '\nPlease enter the name of a city you have visited: '
prompt += "\n(Enter 'quit' when you are finished.)" 

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Using continue in a loop
# Rather than exiting a loop you may want to jump some iterations of the code. Use continue instead break.
current_number = 0
# This piece of code jumps the while loop to the next iteration every time that current_number is even.
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Inifinite Loops
# The while loop depends on some logical statement to exit its execution. If this logical statement does not change its value during the program execution your program will run forever. 
# Example
#while True:
#   print('infinity')

# Using a while Loop with Lists and Dictionaries

# Moving Items from One List to Another
# In this example we will transport values from one list to another one by one.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifing user: ' + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All instances of Specific Values from a List
# The remove() function remove only one instace of the value from a list, we can use the while loop to remove all instances of the value from the list.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input

responses = {}
# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input('\nWhat is your name?')
    response = input('Which mountain would you like to climb someday?')

    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name.title() + ' would you like to climb ' + response + '.')

