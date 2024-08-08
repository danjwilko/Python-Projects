
# A list of dictionaries.
# we could create 3 separate dictionaries for each alien.


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A more realistic example would contain more aliens.

# Empty list for storing the aliens.
aliens = []

# make 30 green aliens.
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.

for alien in aliens[:5]:
    print(alien)

print(f'Total number of aliens: {len(aliens)}')

# The resulting aliens all have the same characteristics however python considers them all separate objects,
# which allows us to modify each individually

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# we could expand the above block by aadding and elif