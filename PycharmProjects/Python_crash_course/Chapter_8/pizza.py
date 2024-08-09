# Storing your functions in modules.

# Importing an entire module.

# To start importing functions, we first need to create a module, A moduel is a file ending in .py that contains the
# code you want to import into your program.

# The code below is going to be the function in the module, that we will import.

def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")