# Using arbitrary keyword arguments.

# Sometimes we will want to accept an arbitrary number of arguments, but we won't know ahead of time what kind of
# information will be past to the function.
# In this case, we can write functions that accept as many key-value pairs as the calling statement provides.

# One such example involves building user profiles: you know you'll get information about a user, but your not sure what
# kind of infomration you'll recieve.

# The function in the following example always takes in a first and last name, but accepts  an arbitrary number of
# keyword arguments as well.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# With this example, the definition expects a first and a last name; it then follows with the double asterisks before
# the parameter. The double asterisk causes Python to create an empty dictionary with the parameter name and put
# whatever key-value pairs it receives into the dictionary.

# Note: You will often see the parameter name **kwargs used to collect non-specific keyword arguments.
