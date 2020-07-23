# This code contains simple examples about working with different data structures (lists, dictionaries...) in Python.

# Nesting

# A list of Dictionaries
# In python you can construct a list compose of dictionaries like the following example:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
# A list in a Dictionary
# Sometimes we want to put an entire list inside a dictionary.
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'exrta cheese']
}

print('You ordered a ' + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

# A Dictionary in a Dictionary
# You can add a dictionary inside a dictionary. Be careful this can make your code complicated quickly.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())

