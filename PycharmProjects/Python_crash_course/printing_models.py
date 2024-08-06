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
# for model in completed_models:
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
    for model in completed_models:
        print(model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

