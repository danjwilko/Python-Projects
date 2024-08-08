# A simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# A dictionary in python is a collection of key-value pairs
# Each key is connected to a value, and you can use the key to access the value associated with the key.

# Accessing Values in a Dictionary To get the value associated with a key, we give the name of the dictionary,
# and then place the key inside a set of square brackets.

# Adding new key-value pairs

alien_0['x_position '] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Here were starting with an empty dictionary and then adding the color and point values to it.

# Typically you'll use an empty dictionary when storing user supplied data in the dictionary, or when you write code
# that generates a large number of key-value pairs automatically

# Modifying Values in a dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0 = {'color': 'yellow'}
print(f"The alien is {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing Key-value pairs

# when you no longer need a piece of information stored in a dictionary, we can use the del statement to completely
# remove the key-value pair.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

