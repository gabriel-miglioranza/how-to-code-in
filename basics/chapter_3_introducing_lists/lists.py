# Author: Gabriel Miglioranza
# Date: 29/05/2019 - 04/06/2019
#
# This code contains simple examples about the use and manipulation of lists in Python.

# What is a list?
# Lists are a collection of items (integers, floats, strings...) in a particular order.
colors = ["red", "green", "blue", "yellow", "black"]
print("This is a list:")
print(colors)

# Accessing elements in a list
# To access a single element in a list use the following syntax:
print("The first element of the list colors is: " + colors[0])
# Index Positions Start at 0, Not 1
# In the example the list colors contains five elements (strings), each element in the list has its own index starting the counter in zero. 
print("colors[0] = " + colors[0])
print("colors[1] = " + colors[1])
print("colors[2] = " + colors[2])
print("colors[3] = " + colors[3])
# The last item in the list can be accessed using the index -1.
print("colors[4] = " + colors[-1])  

# Using Individual Values from a List
# The list colors contains string values. Its possible in python to use items from the list as a simple variable.
print("Goodbye " + colors[3].title() + " Brick Road." )

# Changing, Adding, and Removing Elements

# Modifying Elements in a List
# To change an item in a list just assign a new value using the item index.
print('Colors: ', colors)
# Modifying blue --> purple
colors[2] = 'purple'
print('Colors: ', colors)
# Adding Elements in a List
# Appending Elements to the End of a List
# Using the append() method is the simplest way to add a new item to a list.
print('Colors: ', colors)
colors.append('orange')
print('Colors: ', colors)
# Inserting Elements into a List
# Using the insert() method is possible to choose where (index) the new item is going to be added.
print('Colors: ', colors)
colors.insert(2, 'blue')
print('Colors: ', colors)

# Removing Elements from a List

# Removing an Item Using the del Statement
# Using the del statement is possible to remove an item from a list using its index number.
print('Colors: ', colors)
del colors[2]
print('Colors: ', colors)
# Removing an item Using the pop() Method
# The pop() method removes the last item from a list, and use its value.
print('Colors: ', colors)
last_color = colors.pop()
print('The last color in the list was: ' + last_color)
# Popping Items from any Position in a List
# The pop() method can be used to remove a especific item from a list.
print('Colors: ', colors)
first_color = colors.pop(0)
print('The first color in the list was: ' + first_color)
# Removing an item by Value
# The remove() method can be used to remove an item by its value.
# Note: The remove() method removes only the first occurence of the value in the list.
print('Colors: ', colors)
colors.remove('black')
print('Colors: ', colors)

# Organizing a List

# Sorting a List Pemanently with the sort Method
# The sort() method changes permanently the order (alphabetical/numerical) of items in a list. The sort() method can even be used to put a list in reverse order using sort(reverse=True). 
print('Colors: ', colors)
colors.sort()
print('Colors (Alphabetical): ', colors)
colors.sort(reverse=True)
print('Colors (Reverse Alphabetical): ', colors)
# Sorting a List Temporarily with the sorted() Function
# The sorted() function returns a sorted list, without changing the order of items in the original list.
print('Original colors list: ', colors)
print('Ordered colors list: ', sorted(colors))
print('Original colors list: ', colors)
# Printing a List in Reverse Order
# The reverse() method reverses the order of items in a list (permanently). 
colors.insert(2, 'magenta')
colors.insert(1, 'flicts')
print('Colors: ', colors)
colors.reverse()
print('Colors (Reversed): ', colors)
# Finding the Length of a List
# Using the len() function is possible to obtain the number of items in a list.
print('Colors: ', colors)
print('#colors: ' + str(len(colors)))
# Avoiding Index Errors When Working with Lists
# One type of error is the Index error, it occurs when python tries to access an item in determinated list using an index not contemplated by thath list.
a_list = [1,2,3,35]
print("This is a Index error:")
print(a_list[98])


