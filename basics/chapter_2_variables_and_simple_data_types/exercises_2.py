# Chapter 2 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# Strings - Exercises

# 2-1. Simple Message
simple_message = "Hey, this is a string."
print(simple_message)
# 2-2. Simple Messages
simple_messages = "Hello world!"
print(simple_messages)
simple_messages = simple_messages + "!!!!!!!"
print(simple_messages)
# 2-3. Personal Message
name = " tony moNtaNha   " 
name = name.strip()
name = name.title()
print("Hey "+ name + " would you like to learn some Python today?")
# 2-4. Name Cases
print("Lowercase: " + name.lower())
print("Uppercase: " + name.upper())
print("Titlecase: " + name.title())
# 2-5. Famous Quote
print('Richard Feynman once said, "The first principle is that you must not fool yourself and you are the easiest person to fool."')
# 2-6. Famous Quote 2
famous_person = "Richard Feynman"
famous_quote = "The first principle is that you must not fool yourself and you are the easiest person to fool."
message = famous_person + ' once said, "' + famous_quote + '"'
print(message)
# 2-7. Stripping Names
name = " tony moNtaNha   "
print("\tOriginal: '" + name + "'" + "\n\tlstrip(): '" + name.lstrip() + "'" + "\n\trstrip(): '" + name.rstrip() + "'" + "\n\tstrip(): '" + name.strip() + "'")

# Numbers - Exercises

# 2-8. Number Eight
print("The result from the following expressions is eight:")
print("\t3 + 5 = " + str(3+5))
print("\t16/2 = " + str(16/2))
print("\t2**3 = " + str(2**3))

# 2-9. Favourite Number
favourite = 355/113
print("My favourite number is " + str(favourite) +".")

# 2-10. Adding Comments
# This is a comment

# 2-11. Zen of Python
# Enter import this in a python terminal.