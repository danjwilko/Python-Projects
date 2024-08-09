# Modifying a List in a function.

# When a list ist passed to a function, the function can modify the list.

# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []


# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
#
# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(model)


# We can reorganise this code by writing two functions, each one does a specific job.

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list.
# Sometimes we will want to prevent a function from modifying a list. A way of doing this is by passing the function
# a copy of the original list, so that the original list is not altered.

# function_name(list_name[:])
# """The slice notation [:] makes a copy of the list and sends it to the function"""
