# Author: Gabriel Miglioranza
# Date: 29/05/2019 - 04/06/2019
# Chapter 3 exercises from the book Python Crash Course: A Hands-On, Project-Based Introduction to Programming.

# Lists - Exercises

# 3-1. Names
names = ['Jon', 'Dany', 'Amanda']
print(names)
print("names[0] = " + names[0])
print("names[1] = " + names[1])
print("names[-1] = " + names[-1])
# 3-2. Greetings
print("Hey " + names[0] + ", how are you doing?")
print("Hey " + names[1] + ", how are you doing?")
print("Hey " + names[-1] + ", how are you doing?")
# 3-3. Your Own List
bands = ['The Beatles', 'Queen', 'The Rolling Stones', 'Radiohead', 'Talking Heads', 'Novos Baianos']
print(bands[0] + "is one of the greatest bands of all time.")
# 3-4. Guest List 
guests = ['Richard Feynman', 'Hannah Fry', 'Freddie Mercury']
print('Hey ' + guests[0] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[1] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[2] + " don't you want come over to my place tomorrow? I'll be making dinner.")
# 3-5. Changing Guest List
print(guests[2])
guests[2] = 'Slavoj Žižek'
print('Hey ' + guests[0] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[1] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[2] + " don't you want come over to my place tomorrow? I'll be making dinner.")
# 3-6. More Guests
print("I found a bigger table! Let's invite three more guests.")
guests.insert(0,'Sean Carroll')
guests.insert(2,'Thom Yorke')
guests.append('Ice Cube')
print('Hey ' + guests[0] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[1] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[2] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[3] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[4] + " don't you want come over to my place tomorrow? I'll be making dinner.")
print('Hey ' + guests[5] + " don't you want come over to my place tomorrow? I'll be making dinner.")
# 3-7. Shrinking Guest List
print("The new table won't arrive in time for dinner, sorry but I can only invite two people for today.")
print('Sorry '+ guests.pop(0) + ' but I need to withdraw the invitation for today.')
print('Sorry '+ guests.pop(2) + ' but I need to withdraw the invitation for today.')
print('Sorry '+ guests.pop(1) + ' but I need to withdraw the invitation for today.')
print('Sorry '+ guests.pop(1) + ' but I need to withdraw the invitation for today.')
print(guests[0] + ' you are still invited for dinner today.')
print(guests[1] + ' you are still invited for dinner today.')
del guests[0]
del guests[0]
print(guests)
# 3-8. Seeing the World
places = ['Hong Kong', 'Rio de Janeiro', 'New York', 'London', 'Rome', 'Berlin','Moscow', 'Cape Town']
print('Original list: ', places)
print('Sorted list: ', sorted(places))
print('Original list: ', places)
places_aux = sorted(places)
places_aux.reverse()
print('Sorted and Reversed list: ', places_aux)
places.reverse()
print('Reversed list: ', places)
places.reverse()
print('Original list: ', places)
places.sort()
print('Sorted list: ', places)
places.reverse()
print('Sorted list: ', places)
# 3.9. Dinner Guests 
guests = ['Richard Feynman', 'Hannah Fry', 'Freddie Mercury']
print('I invited ' + str(len(guests)) + " people to today's dinner party.")
# 3.10. Every Function 
scientists = ['Richard Feynman', 'Albert Einstein', 'Niels Bohr', 'Werner Heisenberg', 'Isaac Newton', 'Charles Darwin', 'Marie Curie', 'Stephen Hawking', 'Sean Carroll', 'Carl Sagan', 'Peter Higgs', 'Katie Bouman']
scientists.append('Antoine Lavoisier')
print(scientists)
scientists.insert(4, 'Edwin Powell Hubble')
print(scientists)
scientists.pop(0)
print(scientists)
scientists.remove('Charles Darwin')
print(len(scientists))
print(sorted(scientists))
scientists.sort(reverse=True)
print(scientists)
scientists.reverse()
print(scientists)