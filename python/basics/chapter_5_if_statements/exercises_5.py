# Chapter 5 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# 5-1. Conditional Tests 
# 5-2. More Conditional Tests
print("Is 2 > 3 ? I predict False")
print(2 > 3)

print("Is 200 == 200.0 ? I predict True")
print(200 == 200.0)

car = 'tesla'
print("Is car == 'toyota' ? I predict False")
print(car == 'toyota')

print("Is car == 'Tesla' ? I predict False")
print(car == 'Tesla')

number = 42

print("Is number > 3 and number < 100 ? I predict True")
print(number > 3 and number < 100)

print("Is number != 42 ? I predict False")
print(number != 42)

print("Is number > 10 or number != 42 ? I predict True")
print(number > 10 or number != 42)

colors = ['red', 'green', 'blue']
print("Is 'red' in colors ? I predict True")
print('red' in colors)

print("Is 'black' in colors ? I predict False")
print('black' in colors)

print("Is 'ReD'.lower() in colors ? I predict True")
print('ReD'.lower() in colors)

# 5-3. Alien Colors #1
alien_color = 'green'

if alien_color == 'green':
    print('Congratulations, you earned 5 points.')

# 5-4. Alien Colors #2
if alien_color == 'green':
    print('Congratulations, you earned 5 points.')
else:
    print('Congratulations, you earned 10 points.')

# 5-5. Alien Colors #3
if alien_color == 'green':
    print('Congratulations, you earned 5 points.')
elif alien_color == 'yellow':
    print('Congratulations, you earned 10 points.')
elif alien_color == 'red':
    print('Congratulations, you earned 15 points.')

# 5-6. Stages of Life
age = 5

if age < 2:
    print('baby')
elif age >= 2 and age < 4:
    print('toddler')
elif age >=4 and age < 13:
    print('kid')
elif age >= 13 and age < 20:
    print('teenager')
elif age >= 20 and age < 65:
    print('teenager')
else:
    print('elder')

# 5-7. Favourite Fruit
favourite_fruit = ['bananas', 'apple', 'orange']

if 'bananas' in favourite_fruit:
    print('You really like bananas!')
if 'grape' in favourite_fruit:
    print('You really like grape!')
if 'orange' in favourite_fruit:
    print('You really like orange!')
if 'apple' in favourite_fruit:
    print('You really like apples!')
if 'bananas' in favourite_fruit:
    print('You really like bananas!')

# 5-8. Hello Admin:
usernames = ['admin', 'luke', 'mike', 'anna', 'beth']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + username.title() + ', thank you for logging in again.')

# 5-9. No Users:
usernames = []

if usernames:
    print('We need to find some users!')
else: 
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + username.title() + ', thank you for logging in again.')

# 5-10. Checking Usernames
current_users = ['admin', 'luke', 'mike', 'anna', 'beth']
new_users = ['luKe', 'aNna', 'eric']

for user in new_users:
    if user.lower() in current_users:
        print('The username ' + user + ' is already in use, try a new one.')
    else:
        print('Welcome '+ user.title() +'!')

# 5-11. Ordinal Numbers
numbers = range(1,10)
for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')

# 5-12. Styling if statements
# 5-13. Your Ideas
