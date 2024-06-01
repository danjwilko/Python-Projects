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


