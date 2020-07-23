# Chapter 4 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# Lists

# 4-1. Pizzas
flavors = ['margherita','pepperoni','four cheese']
for flavor in flavors:
    print('I like ' + flavor + ' pizza.')
print('I really love pizza!')

# 4-2 Animals
animals = ['dogs', 'platypuses', 'kiwis', 'cats','koala']
for animal in animals:
    print(animal.title() + ' are beautiful animals.')
print('These are examples of warm-blooded animals.')

# 4-3. Counting to Twenty
for value in range(1,21):
    print(value)

# 4-4. One Million 
one_million_numbers = range(1,int(1e6)+1)
print(max(one_million_numbers))
print(min(one_million_numbers))
print(sum(one_million_numbers))

# 4-6. Odd Numbers
odd_numbers = range(1,21,2)
for number in odd_numbers:
    print(number)

# 4-7. Threes
multiples_of_3 = [value*3 for value in range(1,11)]
for multiple in multiples_of_3:
    print(multiple)

# 4-8. Cubes
cubes = []
for value in range(1,11):
    cubes.append(value**3)

# 4-9. Cube Comprehension 
cubes_comprehension = [value**3 for value in range(1,11)]
print(cubes == cubes_comprehension)

# 4-10. Slices
print('The first three items in this list are:')
for animal in animals[:3]:
    print(animal)
print('Three items from the middle of the list are:')
for animal in animals[1:4]:
    print(animal)
print('The last three items in the list are:')
for animal in animals[-3:]:
    print(animal)

# 4-11. My Pizzas, Your Pizzas
friend_flavors = flavors[:]
friend_flavors.append('supreme') 

print('My favorite pizzas are:')
print(flavors)
print("My friend's favorite pizzas are:")
print(friend_flavors)

# 4-12 More Loops
print('My favorite pizzas are:')
for flavor in flavors:
    print(flavor)
print("My friend's favorite pizzas are:")
for flavor in friend_flavors:
    print(flavor)

# Tuples

# 4-13. Buffet
buffet = ('pizza', 'hamburger', 'sushi','bread','french fries')
print('Original menu:')
for meal in buffet:
    print(meal)
#buffet[3] = 'rice' # this line of code is rejected by Python.
buffet = ('pizza', 'hamburger', 'sushi','rice','french fries')
print('New menu:')
for meal in buffet:
    print(meal)

