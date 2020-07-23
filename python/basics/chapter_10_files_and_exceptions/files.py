# This code contains simple examples about working with files in Python.

# Reading an Entire File
# Let's do a simple example. In the nest session, we want to open a 
# file named pi_digits.txt. This file contains the numerical value of pi. 
# Let's get read this number in the file and display in the screen. 
# First, we open the file inside a context manager. 
# A context manager is constructed using the word 'with', inside a context
# manager exists some variables specific for this context 
# (block of code), hence the name 'context manager'.
# 
# In this example we use the open() function with the file name as 
# parameter. We put the return from the open() function into the file_object
# variable and use into the idented space. 
# Into the idented space (block of code/context manager) we can read the 
# content from the file using the function read(). The return value from
# this function is the content from the file 'pi_digits.txt', stored into
# the 'contents' variable. 
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# File Path
# To open a file we need to give a the file location inside your 
# operational system(OS). To access some file in your OS, you can pass
# into the open() function the absolute file location or the 
# relative file location. In a Linux system you can discover the actual 
# folder path using 'pwd'. The relative location from the
# folder that your python script is stored. 

with open('./pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Reading Line by Line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print('-------------------')
        print(line.rstrip())
    
    print('-------------------')

# Making a List of Lines from File 
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with a File's Contents
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)

# Large Files: One Million Digits
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string[:52]+ '...')
print(len(pi_string))

# Is Your Birthday Contained in Pi?
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else: 
    print('Your birthday does not appear in the first million digits of pi.')

