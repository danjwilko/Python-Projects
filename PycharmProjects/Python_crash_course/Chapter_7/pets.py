# Removing all instances of specific values from a list.
# Using remove() would remove one instance not repeated items.
# We can use the while loop and 'in' key word so that while the list
# contains the matching items, they will be removed.

# The following list has multiple instances of 'cat'.
pets = ['dog','cat', 'dog', 'goldfish', 'cat', ' rabbit', 'cat']
print(pets)

# looping through the list seeing if 'cat' in the list, if it is removing the 'cat' item.
while 'cat' in pets:
    pets.remove('cat')

# printing the final list.
print(pets)


