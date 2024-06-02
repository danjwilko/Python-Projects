# Checking for inequality

# when you want to determine whether two values are not equal we can combine the ! and the  = , != means is
# not equal

# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#    print('Hold the anchovies')

# Numerical Comparisons
# answer = 17

# if answer != 42:
#    print("That is not the correct answer, Please try again!")

# Checking multiple conditions
# You may want to check multiple conditions at the same time, for example you may need two
# conditions to be true to take an action.

# Using and to check.

age_0 = 22
age_1 = 18
if age_0 > 21 and age_1 > 21:
    print(True)
else:
    print(False)

# Using or to check for inequality

age_0 = 22
age_1 = 18
if age_0 > 21 or age_1 > 21:
    print(True)
else:
    print(False)

# Checking whether a value is in a list.

# To find out if a item is in a list we can use the key word 'in'

requested_toppings = ['mushrooms', 'onion', 'pineapple']
if 'mushrooms' in requested_toppings:
    print(True)
else:
    print(False)

if 'pepperoni' in requested_toppings:
    print(True)
else:
    print(False)

# # Testing multiple Conditions p83.
#
# # Sometimes It's important to test for each condition. So we can use several if statements.

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print(f"\nFinished making your pizza!")

# This code wouldn't work properly if we used an if-elif-else block, it would stop running after meeting the
# conditions of one of the tests.
# This way each condition is tested.

# Checking for special items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

# if the restaurant runs out of an ingredient:
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}")


# Checking a list is not empty, we've assumed so far each list has items in it but what happens when using user input
# for example?
# We can no longer assume a list is not empty.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists:

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we dont have {requested_topping}")
print("\nFinished making your pizza!")
