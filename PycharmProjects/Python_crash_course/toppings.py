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
if age_0 >= 21 and age_1 > 21:
    print(True)
else:
    print(False)

# Using or to check for inequality

age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 > 21:
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

