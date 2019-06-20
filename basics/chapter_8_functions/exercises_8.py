# Chapter 8 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# 8-1. Message
def display_message():
    '''Display a simple message'''
    print('Python is great!')

display_message()

# 8-2. Favorite Book
def favorite_book(title):
    """Display your favorite book's title."""
    print('One of my favorite books is ' + title.title() + '.')

favorite_book('against method')

# 8-3. T-Shirt
def make_shirt(size, message):
    '''Make a shirt with the desired size and message'''
    print('Shirt size:' + size)
    print('Message in the shirt: ' + message)

make_shirt('M', 'The Beatles')
make_shirt(size='M', message='Radiohead')

# 8-4. Large Shirts
def make_shirt(size='XG', message='I love Python!'):
    '''Make a shirt with the desired size and message'''
    print('Shirt size:' + size)
    print('Message in the shirt: ' + message)

make_shirt()
make_shirt('M')
make_shirt('P', 'Radiohead')

# 8-5. Cities
def describe_city(city, country='brazil'):
    '''Display a simple information about a city'''
    print(city.title() + ' is in ' + country.title() + '.')

describe_city('são paulo')
describe_city('london', 'england')
describe_city(city='brasília')

# 8-6. City Names
def city_country(city, country):
    return city.title() + ', ' + country.title()

print(city_country('manaus','brazil')) 

# 8-7. Album
def make_album(artist, title, n_tracks=0):
    album = {'artist': artist, 'title': title}
    if n_tracks != 0:
        album['number of tracks'] = n_tracks
    return album

ok_computer = make_album('radiohead', 'ok computer', 12)
sgt_peppers = make_album('the beatles', "sgt. pepper's lonely hearts club band")
print(ok_computer)
print(sgt_peppers)

# 8-8. User Albums
while True:
    print("\nPlease describe a music album:")
    print("(enter 'q' at any time to quit)")
    t_name = input('Title: ')
    if t_name == 'q':
        break
    a_name = input('Artist: ')
    if a_name == 'q':
        break
    number = input('Number of tracks (default = 0): ')
    if number == 'q':
        break
    album = make_album(a_name, t_name, int(number))
    print(album)
print('Goodbye!')

# 8-9. Magicians
def show_magicians(magicians):
    '''Show magicians' names.'''
    for magician in magicians:
        print(magician.title())

magicians = ['david copperfield', 'robert angier', 'alfred borden']
show_magicians(magicians)

# 8-10. Great Magicians
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the great '+ magicians[i]
    return magicians


show_magicians(make_great(magicians[:]))

# 8-11. Uncharged Magicians
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
show_magicians(magicians)

# 8-12. Sandwiches
def make_sandwich(*items):
    '''Summarize the sandwich we are about to make.'''
    print('Making a sandwich with the following items:')
    for item in items:
        print('- ' + item)

make_sandwich('pastrami', 'cheese')
make_sandwich('bread')
make_sandwich('cheese', 'ham', 'bacon')

def build_profile(first, last, **user_info):
    '''Build a dictionary containig everything we know about the user.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('tony','montanha', age=4, breed='shih tzu')

# 8-14. Cars
def build_car(manufacturer, model, **car_info):
    '''Building a dictionary containig everything we know about a car.'''
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8-15. Printing Models
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

# 8-16. Imports
# 8-17. Styling Functions 