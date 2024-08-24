from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


dice6 = Die()

results = []
for num in range(10):
    result = dice6.roll_die()
    results.append(result)
print(f"10 rolls of a 6 sided dice.")
print(results)


dice10 = Die(sides=20)

results = []
for num in range(20):
    result = dice10.roll_die()
    results.append(result)
print(f"10 rolls of a 20 sided dice.")
print(results)

