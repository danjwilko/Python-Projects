# If statements
# Pythons if statements allows you to examine the current state of a program,
# and respond appropriately to that state.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars :
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# At the heart of every if statement is an expression that can be evaluated as True of False, and is called
# a conditional test.

# Checking fot Equality.
"""
car = 'bmw'
car == 'bmw'
# this will return true

car = 'Audi'
car == 'audi'
# This will return False
"""

# Ignoring Case when checking for Equality.

"""
car = 'Audi'
car.lower() == 'audi' 
# This will return True
"""

