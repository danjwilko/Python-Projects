# Passing an arbitary number of arguments.

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green pepper', 'extra cheese')

# The asteriks * tells python to creat an empty tuple called toppings and pack whatever values it receives into it.

def make_pizza(*toppings):
    """Summarise the pizza we are about to make"""
    print(f"Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')