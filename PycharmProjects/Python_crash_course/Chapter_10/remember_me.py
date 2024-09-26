# import json
#
# username = input("What is your name? ")
#
# filename = 'username.json'
#
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back {username}!")
#

# Were now going to combine the two programs into one

#import json

# Load the username if it has been stored previously.
# Otherwise, prompt for the username and store it.

# filename  = 'username.json'
#
# try:
#     with open (filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open (filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}")
# else:
#     print(f"Welcome back, {username}")


# #Refactoring
# Often, you'll come to a point where your code will wor, but you recognise that
# you could improve the code by breaking it up into a series of functions that have specific jobs.
# The process is called refactoring.
# Refactoring makes your code cleaner and easier to extend.

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet te user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")
greet_user()



