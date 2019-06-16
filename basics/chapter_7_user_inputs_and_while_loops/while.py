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