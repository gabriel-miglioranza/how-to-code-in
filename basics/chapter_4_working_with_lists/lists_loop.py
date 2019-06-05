# Author: Gabriel Miglioranza
# Date: 05/06/2019 - 
#
# This code contains simple examples about working with lists in Python.

# Looping Through an Entire List
# The for loop can be used to repeat an operation through an entire list. The syntax is as follows:
magicians = ['alice', 'david', 'robert', 'maria']
for magician in magicians:
    print(magician)
# A Closer Look at Looping
# In this piece of code we put each item, one at a time, from the list 'magicians' on the 'magician' variable, and print it out. The 'magician' variable holds the value of the last item accessed by the for loop.
print('The last magician in the list is: ' + magician)
# Doing More Within a for Loop
# Just an example on how an item in the for loop can be used:
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
# Doing Something After a for Loop
# Python knows what is in and out the for loop from code indentation.
for magician in magicians:
    # Inside the for Loop
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    # Inside the for Loop
# Outside the for Loop
print('Thank you, everyone. That was a great magic show!')

# Avoiding Identation Errors

# Forgetting to Indent 
# When Python expects an indent block and doesn't find one (after a for statement for example), it lets you know which line it had a problem with.
# Remove the #'s from the next two lines and run the program to see the result. 
# for magicians in magician:
# print(magician)
# Forgetting to Indent Additional Lines
