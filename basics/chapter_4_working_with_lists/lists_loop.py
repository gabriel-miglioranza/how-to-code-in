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
#for magicians in magician:
#print(magician)

# Forgetting to Indent Additional Lines
# In contrast with the syntax errors, we have logic errors, an example is forgetting to indent additional lines. The python interpreter is not going to return an syntax error, but if you forget to indent a line that should be in the for loop, your code will not present the desired output.
for magician in magicians:
    # Inside the for Loop
    print(magician.title() + ', that was a great trick!')
    # Inside the for Loop
# Outside the for Loop
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Indenting Unnecessarily
# If by accident you indent unnecessarily Python will report that error.
# Remove the #'s from the next two lines and run the program to see the result. 
#   print(magician)

# Indenting Unnecessarily After the Loop
# If you indent unnecessarily after a loop you will fall into a logic error. Python will accept you syntax, but the scripts will not return the desired result.
for magician in magicians:
    # Inside the for Loop
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print('Thank you, everyone. That was a great magic show!')
    # Inside the for Loop
# Outside the for Loop

# Forgetting the Colon
# The colon (:) tells Python to interpret the next line as a loop start, if you forget to put it, an syntax error is displayed at your screen.
# Remove the #'s from the next two lines and run the program to see the result. 
# for magicians in magician
#   print(magician)

# Making Numerical Lists

# Using the range() Function
# The range() function is used to generate a sequence of integer numbers.
# In the example next example will print the numbers from 1 to 4 = {1,2,3,4}
for value in range(1,5):
    print(value)

# Using range() to Make a List of Numbers
# To store a sequence of numbers in a list, you can use the list() function combined with the range() function.
print('List of numbers from 1 to 5: ')
numbers = list(range(1,6))
print(numbers)
# You can create a diverse set of sequences with the range() function.
print('Sequence of even numbers from 0 to 20: ')
even_numbers = list(range(0,21,2))
print(even_numbers)
print('Sequence of areas from squares with side lengths from 1 to 10:')
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Simple Statistics with a list of Numbers
# The function min() returns the minimum value from a list of numbers.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min_digits = min(digits)
print(min_digits)
# The function max() returns the maximum value from a list of numbers.
max_digits = max(digits)
print(max_digits)
# The function sum() returns the summation of a list of numbers.
sum_digits = sum(digits)
print(sum_digits)
# List Comprehensions
# To generate the list with a sequence of areas from squares with side lengths from 1 to 10, we used three lines. With list cromprehension is possible to obtain the same result with one line of code. The next example builds this list with one line:
squares = [value**2 for value in range(1,11)]
