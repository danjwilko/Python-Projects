# Returning a dictionary.
# A function can return any kind of value you need it to, including more complicated data structures like:
# Lists and dictionaries.

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi','hendrix')
print(musician)


# We can extend the above function to include optional values like a middle name or an age, or occupation etc.



def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi','hendrix', age=27)
print(musician)
