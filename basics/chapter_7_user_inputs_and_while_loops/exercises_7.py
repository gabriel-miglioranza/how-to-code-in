# Chapter 7 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# 7-1. Rental Car
car = input('Which car do you want to rent?')
print('Let me see if I can find you a '+ car + '.')

# 7-2. Restaurant Seating
number = input('How many people come to dinner?')
number = int(number)

if number > 8:
    print('Sorry, but there is none table available for your group right now, can you wait for a little?')
else:
    print('Your table is ready.')
# 7-3 Multiples of Ten
number = input('Please type a number: ')
number = int(number)
if number % 10 == 0:
    print('Your number is a multiple of 10.')
else:
    print('Your number is not a multiple of 10.')

    