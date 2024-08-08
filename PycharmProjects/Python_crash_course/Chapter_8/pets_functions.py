# Note on passing arguments to the functions. As a function definition can have multiple parameters, a function call
# may need to have multiple arguments to pass in.
# We can use positional arguments to pass into the function which need to be in the same order as the parameters.
# We can use keyword arguments, each argument consists of a variable name & value & lists and dictionaries of values.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword argument example.

describe_pet(pet_name='harry', animal_type='hamster')


# Default values.
# When writing a function, you can define a default value for each parameter.
# If a argument for a parameter is provided, then the function will use the argument value,
# otherwise it will use the dfault value.

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')

# Equivalent Function calls. Because positional arguments, keyword arguments, and default values can all be used
# together, often you'll have several equivalent ways to call a function.

# For this definition, we will always need to provide an argument for the pet_name parameter.

# describe_pet(pet_name, animal_type="dog")

# This value can be provided using the positional or keyword format.
# A dog named Willie.
describe_pet(pet_name='willie')
describe_pet(pet_name='willie')

# A hamster named Harry.

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument errors.


def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet()
# Python recognises that some information is missing from the function call and the traceback tells us that:

# Traceback (most recent call last): File "/home/daniel/Documents/Github
# files/Python-Projects/PycharmProjects/Python_crash_course/pets_functions.py", line 58, in <module> describe_pet()
# TypeError: describe_pet() missing 1 required positional argument: 'pet_name'





