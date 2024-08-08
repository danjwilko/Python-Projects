# Alien Colors 5-3

alien_color = 'green'

if alien_color == 'green':
    print("You have just earned 5 points")

# version that will fail.
alien_color = 'yellow'
if alien_color == 'green':
    print("You have just earned 5 points.")


alien_color = 'red'

if alien_color == 'green':
    points = 5
if alien_color == 'red' or alien_color == 'yellow':
    points = 10

print(f"You have just earned {points}.")

# using the else block.
alien_color = 'red'

if alien_color == 'green':
    points = 5
else:
    points = 10

print(f"You have just earned {points}.")

# if-elif-else

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"You have just earned {points}.")

stage_of_life = ''
age = 20

if age < 2:
    stage_of_life = 'Baby'
elif 2 <= age < 4:
    stage_of_life = 'toddler'
elif 4 <= age < 13:
    stage_of_life = 'kid'
elif 13 <= age < 20:
    stage_of_life = 'teenager'
elif 20 <= age < 65:
    stage_of_life = 'adult'
else:
    stage_of_life = 'elder'

print(f"The persons is an {stage_of_life}.")




