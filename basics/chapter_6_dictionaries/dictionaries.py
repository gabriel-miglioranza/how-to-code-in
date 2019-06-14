# This code contains simple examples about the use and manipulation of dictionaries in Python.

# A Simple Dictionary
# Working with Dictionaries
# A dictionary is a data structure that connect a key and an item, list, other dictionary (key-value pairs). 

alien_0 = {'color': 'green', 'points': 5}

# Acessing Values in a Dictionary
# To get an specific value from a dictionary, use the name of the dictionary and the key inside brackets.
print(alien_0['color'])
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

# Adding New Key-Value Pairs
# To add a new key-value pair in your dictionary use the following syntax:
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
# Want to star an empty dictionary? Just do this:
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a Dictionary
# To change a value from a key-value pair just use the same syntax as if you are adding a new key-value pair.
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow' 
print('The alien is now ' + alien_0['color'] + '.')

# Removing Key-Value Pairs
# When you want to remove some key-value pairs, use the command del.
print(alien_0)
del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
# A dictionary can be used to storing different kinds of information about one object.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favourite language is " + favourite_languages['sarah'].title() + ".")

# Looping Through a Dictionary

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'last': 'enrico',
    'last': 'fermi'
}
# To loop through every key-value use this syntax:
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# Another example
for name, language in favorite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

# Looping Through All Keys in a Dictionary
# Printing all key values
for key in user_0:
    print(key)
for key in user_0.keys():
    print(key)

# Looping Through a Dictionary's Keys in Order
# To get the keys in a alphabetical order use the sorted() function.
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping Through All Values in a Dictionary
# The method values() return a list with all values in a dictionary.
for language in favorite_languages.values():
    print(language.title())
# This approach returns all the values from a dictionary. If you want to return only unique items use the set() function
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
