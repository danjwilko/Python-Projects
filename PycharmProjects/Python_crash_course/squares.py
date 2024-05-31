# Making numerical lists.

# Using the range() function.
# the range function can be used to generate a series of numbers, for example:

# note it will print each value within the range but not 5.(off-by one behavior in programming). The range function
# causes python to start counting at the first value you give it and stop when it reaches the second value,
# because it stops at the second value, the output never contains the end value.

for value in range(1, 5):
    print(value)


for value in range(1, 6):
    print(value)

# Using range() to make a list of numbers

numbers = list(range(1, 6))
print(numbers)

# We can also  give range() a third argument, to skip numbers.
# This third value is used as a step size when generating numbers.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Use two asteriks, to denote exponents. (**).
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# To make the code more conice we can omit the temporary variable square, and append each value directly to the list.

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Simple statistics
# we can use min(), max() and sum().

squares = [value ** 2 for value in range(1, 11)]
print(squares)


