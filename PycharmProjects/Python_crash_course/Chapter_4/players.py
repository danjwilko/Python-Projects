# Working with part of a list.

# Slicing a list.

# To slice a list , you specify the index of the first and the last elements you want to work with.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

# missing the start index, python automatically starts, your slice at the beginning of the list.

print(players[:4])

# similarly, if we miss the last index, python will automatically run from the first index until the end of the list.

print(players[2:])

# negative values, this index value will print the last 3 items of the list.
print(players[-3:])

# similarly, this will print from the start of the list omitting the last 3.
print(players[:-3])

# Looping through a slice.

print('Here are the first three players on my team')
for player in players[:3]:
    print(player.title())
