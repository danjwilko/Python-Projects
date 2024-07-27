# A list in a dictionary

# Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a dictionary. As an
# example, if we were to describe a pizza someone was ordering if we used a list, we could really only store is a list
# of the toppings.
# With a dictionary, a list of toppings can be just one aspect of the pizza we are describing.


# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarise the order.

print(f"You ordered a {pizza['crust']}-crust pizza ""with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

