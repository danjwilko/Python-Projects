# Defining a tuple
""" A tuple looks just like a list except we use parenthesis instead of square brackets."""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# when trying to modify a tuple we get an error as it cannot be done with that type.
# dimensions[0] = 250

# note Tuples are technically defined by the presence of a comma; the parentheses make them
# look neater and more readable. If you want to define a tuple with 1 element you need to include a trailing comma.

# my_t = (3,)

# Looping through all the values in a tuple.

#for dimension in dimensions:
#    print(dimension)

# Writing over a tuple.

# Although you cannot modify a tuple, you can assign a new variable that represents a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple.
# In this way were not modifying the existing tuple but redefining the variable.

print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

for dimension in dimensions:
    print(dimension)
