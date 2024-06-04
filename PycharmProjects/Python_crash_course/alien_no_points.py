# Using get() to Access Values.

alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points'])
# This results in an error, well learn how to handle these later.

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

# If there's a chance the key your asking for doesnt exist within the dictionary, we should consider using get(),
# instead of the square bracket notation.

