# This code contains simple examples about the use and manipulation of tuples in Python.

# Tuples 
# The tuple looks like a list except you use parentheses instead of square brackets.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# The tuple 'dimensions' is defined using parentheses instead of brackets.
# The great difference between a tuple and a list is that you can't assign a new value to an tuple item.

# Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
# Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple.
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

