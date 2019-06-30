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

# 7-3. Multiples of Ten
number = input('Please type a number: ')
number = int(number)
if number % 10 == 0:
    print('Your number is a multiple of 10.')
else:
    print('Your number is not a multiple of 10.')

# 7-4. Pizza Toppings
pizza_toppings = []
print('Hello! Which pizza toppings do you desire?')
prompt = '\nPlease enter the topping you want:'
prompt += "\n(Enter 'quit' when you have finished.)"

while True:
    message = input(prompt)

    if message == 'quit':
        if pizza_toppings:
            print('Plain pizza it is then.')
        else:
            print('Your pizza toppings are:')
            print(pizza_toppings)
        break
    else:
        pizza_toppings.append(message) 

# 7-5. Movie Tickets

prompt = '\nPlease enter your age: '
prompt += "\n(Enter 'quit' when you have finished.)"
while True:
    age = input(prompt)
    if age == 'quit': break
    
    age = int(age)
    if age < 3:
        print('Your ticket is free.') 
    elif age >=3 and age < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')

# 7-6. Three Exits
# 7-7. Infinity
#while True:
#   print('infinity')

# 7-8. Deli
sandwich_orders = ['bacon', 'pastrami', 'bagel toast', 'baloney', 'pastrami', 'barbecue', 'doner kebab', 'pastrami']
finished_sandwishes = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print('I made your ' + sandwich + 'sandwich.')

print('I made these sandwiches:')
print(set(finished_sandwishes))

# 7-9. No Pastrami
sandwich_orders = ['bacon', 'pastrami', 'bagel toast', 'baloney', 'pastrami', 'barbecue', 'doner kebab', 'pastrami']
finished_sandwishes = []

print('Deli has run out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print('I made your ' + sandwich + 'sandwich.')

print('I made these sandwiches:')
print(set(finished_sandwishes))

# 7-10. Dream Vacation
dream_vacation = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name?')
    response = input('If you could visit one place in the world, where would you go?')

    dream_vacation[name] = response

    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False

for name, response in dream_vacation.items():
    print(name.title() + ' would you like to go to ' + response.title() + '.')