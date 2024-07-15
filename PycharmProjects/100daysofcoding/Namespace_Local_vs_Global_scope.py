enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope

#def drink_potion():
#    potion_strength = 2
#    print(potion_strength)


#drink_potion()
#print(potion_strength)

# Global scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

# Python does not have block scope

if 3 > 2:
  a_variable = 10

game_level = 3
enemies = ['skeleton','zombie', 'alien']
if game_level < 5
  new_enemy = enemies[0]

