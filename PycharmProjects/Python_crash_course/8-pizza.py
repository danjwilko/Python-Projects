# Passing an arbitrary number of arguments.

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


# Mixing positional and arbitrary arguments.

# If we want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number
# of arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first, then collects any remaining arguments in the final parameter.


def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

# Note: You will often see the generic parameter name *args, which collects arbitrary positional arguments like this.

