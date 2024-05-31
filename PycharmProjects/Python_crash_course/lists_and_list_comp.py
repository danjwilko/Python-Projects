# counting to twenty.

numbers = []
for value in range(1, 21):
    print(value)

# One in a million.
for value in range(1, 1000001):
    numbers.append(value)
print(numbers)

# summing a million
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Odd numbers
odd_numbers = []
for value in range(1, 20, 2):
    odd_numbers.append(value)
print(odd_numbers)
# Three's
threes = []
for value in range(3, 31, 3):
    threes.append(value)
print(threes)

# Cubes
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

# cube comprehension

cube_comp = [value ** 3 for value in range(1, 11)]
print(cube_comp)