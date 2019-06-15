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
    'dictionary': 'collection of key-value pairs.',
    'string': 'a collection of characters in a certain order.',
}

print('List: ' + glossary['list'])
print('Tuple: ' + glossary['tuple'])
print('Dictionary: ' + glossary['dictionary'])

# 6-4 Glossary 2
for key, value in glossary.items():
    print(key.title() + ': ' + value)

# 6-5. Rivers
rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'são francisco': 'brazil'
}

for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.')

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_poll = ['jen', 'sarah', 'ned', 'phil', 'james']

for people in people_poll:
    if people in favorite_languages.keys():
        print(people.title() + ', thanks for your answer.')
    else:
        print(people.title() + ', you have not taken the poll yet.')

# 6-7. People 
person_0 = {
    'first_name': 'sean',
    'last_name': 'carroll',
    'city': 'los angeles'
}

person_1 = {
    'first_name': 'hannah',
    'last_name': 'fry',
    'city': 'london'
}

person_2 = {
    'first_name': 'gabriel',
    'last_name': 'miglioranza',
    'city': 'porto alegre'
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = person['first_name'] + ' ' + person['last_name']
    city = person['city']
    print(full_name.title() + ' lives in ' + city.title() + '.')

# 6-8 Pets
montanha = {
    'kind': 'dog',
    'owner': 'gabriel'
}

chiara = {
    'kind': 'cat',
    'owner': 'amanda'
}

guri = {
    'kind': 'dog',
    'owner': 'ito'
}

pets = [montanha, chiara, guri]

for pet in pets:
    for key, value in pet.items():
        print(key.title() + ': ' + value.title())

# 6-9. Favorite Places
favorite_places = {
    'anna': ['angel falls', 'antartica', 'antelope canion'],
    'paul': ['the azores', 'boracay', 'cabo san lucas'],
    'miguel': ['grand canyon', 'faroe islands', 'fernando de noronha']
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are:")
    for place in places:
        print('\t' + place.title() + '.')

# 6-10. Favorite Numbers
favorite_numbers = {
    'cris': [234, 3434, 343],
    'bianca': [215423, 534, 3523],
    'monica': [42, 3454, 345]
}

for name, numbers in favorite_numbers.items():
    print(name.title() + ': ', numbers)

# 6-11. Cities
cities = {
    'porto alegre':{
        'contry': 'brazil',
        'population': '1479101',
        'foundation': '1772 AC'
    },
    'new york city':{
        'contry': 'united states of america',
        'population': '8175133',
        'foundation': '1898 AC'
    },
    'rome':{
        'contry': 'italy',
        'population': '2872800',
        'foundation': '753 BC'
    }
}

for city, infos in cities.items():
    print('About ' + city.title() + ':')
    for key, info in infos.items():
        print(key.title() + ': ' + info.title())

# 6-12. Extensions