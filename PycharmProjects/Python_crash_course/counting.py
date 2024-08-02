# Introducing while loops.

# We can use a while loop to count up through a series of numbers.
# current_number = 1
# Python will repeat the loop as long as the condition is met.
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# This program will print out each number from 1-5 inclusive on a new line.

# You can use the break statement in any of python's loops. For example, you could use break to quit
# a for loop that's working through a list or a dictionary.

"""Using the continue statement in a loop"""
# Rather than breaking out of a loop entirely, we can use the continue statement to return to the beginning of the loop
# based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

"""Avoiding Infinite loops"""
x = 1
while x <= 5:
    print(x)
    # As an example if we missed the next line from the program this while loop would run forever.
    x += 1
