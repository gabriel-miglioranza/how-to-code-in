# Chapter 6 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# 6-1. Person
person = {
    'first_name': 'sean',
    'last_name': 'carroll',
    'city': 'los angeles'
}

print(person)

# 6-2. Favorite Numbers
favorite_numbers = {
    'cris': 23,
    'bianca': 133,
    'monica': 42
}

print("Monica's favorite number is " + str(favorite_numbers['monica']) + ".")
print("Cris' favorite number is " + str(favorite_numbers['cris']) + ".")
print("Biancas's favorite number is " + str(favorite_numbers['bianca']) + ".")

# 6-3 Glossary
glossary = {
    'list': 'set of values organized in a cardinal order.',
    'tuple': "set of fixed values organized in a cardinal order.",
    'dictionary': 'collection of key-value pairs.'
}

print('List: ' + glossary['list'])
print('Tuple: ' + glossary['tuple'])
print('Dictionary: ' + glossary['dictionary'])