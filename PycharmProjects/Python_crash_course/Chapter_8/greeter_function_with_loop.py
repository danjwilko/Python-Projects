# We can use functions with all the the Python structures we've learned about so far.
# For example, the following function used with a loop.

# def get_formatted_name(first_name, last_name):
#     """Return a full name formatted neatly."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}!")

# Here we've used a version that doesn't use middle names.
# We also haven't enabled a quit condition.


def get_formatted_name(first_name, last_name):
    """Return a full name formatted neatly."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")
