# Author: Gabriel Miglioranza
# Date: 29/05/2019
#
# This code contains simple examples about the use and manipulation of strings in Python.

# A string is a sequence of characters, anything between "" or '' is considered a string in python.

string_1 = "This is a string."
string_2 = 'This is another string.'
print(string_1)
print(string_2)

# Changing case in a string with Methods

name = "tony montaNha"
print("Original string: " + name)
# Method .title() change the string to a title pattern. The first letter in each word is upper case and the remain in lower case.
print("Title Method: " + name.title())
# Method . upper() makes every character upper case.
print("Upper Method: " + name.upper())
# Method .lower() makes every character lower case.
print("Lower Method: " + name.lower())

# Combining or Concatenating strings

first_name = "tony"
print("First name: " + first_name)
last_name = "montanha"
print("Last Name: " + last_name )
# Use + to concatenate two or more strings. Ex: "tony" + " " + "montanha" = "tony montanha"
full_name = first_name + " " + last_name
print("Full name: " + full_name)
# Another example
print("Hello, " + full_name.title() + "!")

# Adding Whitespace to Strings with Tabs or Newlines

# Use \t to adds a tab in the string.
print("Python")
print("\tPython")
# To add a new line use \n in the string
print("This text is in one line.")
print("This\ntext\nhave\nmuliple\nlines!")

# Stripping Whitespace

# The rsptrip() method removes extra whitespaces at the right end of a string.
favorite_language = 'python '
print("String with extra whitespace:" + favorite_language + "!")
print("String without extra whitespace:" + favorite_language.rstrip() + "!")
# lstrip() and strip() methods are a variation of rtrip() method. The former removes the left side extra whitespaces, and The latter removes whitespaces from both end an beginning of the string.
a_string = "    This is a string!   "
print("Original string: " "'"+ a_string +"'" )
print("lstrip() string: " "'"+ a_string.lstrip() +"'" )
print("strip() string: " "'"+ a_string.strip() +"'" )

    