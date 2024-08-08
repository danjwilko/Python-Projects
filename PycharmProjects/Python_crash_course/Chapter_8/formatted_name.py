# Returning a simple value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Making an Argument Optional

# Sometimes it makes sense to make an argument optional so that people using the function can choose to provide
# extra information only if they want to. We can use default values to make the arguments optional.

# for example


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# This above function works when given a first, middle and a last name. However, if, for example, we omitted the middle
# name, it wouldn't work.

# To make the function work without the middle name, we set the default value of middle name to an empty string and move
# it to the end of the list of parameters.


def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)



