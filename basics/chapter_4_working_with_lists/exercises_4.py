# Chapter 4 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# Lists

# 4-1. Pizzas
flavours = ['margherita','pepperoni','cheese']
for flavour in flavours:
    print('I like ' + flavour + ' pizza.')
print('I really love pizza!')

# 4-2 Animals
animals = ['dogs', 'platypuses', 'kiwis', 'cats']
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