# Passing a list to a function.
# When a list gets passed to a function, the function gets direct access to the contents of the list.

# Example: we have a list of users, and want to print a greeting to each.

def greet_users(names):
    """Print a simpe greeting to each user in the list"""
    for name in names:
        msg = f'Hello {name.title()}'
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

