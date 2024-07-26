
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
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)

# Show the first 5 aliens.

for alien in aliens[:5]:
    print(alien)

print(f'Total number of aliens: {len(aliens)}')

# The resulting aliens all have the same characteristics however python considers them all separate objects.
