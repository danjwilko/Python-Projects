# Simple function that prints a greeting.


# The first line is defining the function.
# def greet_user():
#     # docstring which describes what the function does.
#     """Display a simple greeting."""
#     # print the message.
#     print("Hello!")
#
#
# # Calling the function.
# greet_user()


# Passing information to a function.

# We can modify the above code slightly to greet them by name.

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")


greet_user('jesse')


