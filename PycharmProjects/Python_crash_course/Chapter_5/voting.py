# If statements

# simplest if statement is:

"""
if conditional_test:
    do something
"""

age = 19
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
    # If the person was younger than 18 we would receive no output.
    # pythons if-else statements enable use to have additional sets of conditional tests.
# Add in a if-else statement
else:
    print("You are too young to vote")
    print("Please register to vote as soon as you turn 18!")


# Using if-elif-else.

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")


# to be more concise:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")


# Using multiple elif blocks

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# Omitting the else block.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

# by omitting the general catch-all else block, we have given the data a condition it has to pass.
