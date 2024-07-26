"""This method we are using the key, value pairs still just with the nme changed to name and language for easier
readability and understanding."""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# for name, language in favorite_languages.items():
#     print(f"{name.title()} 's favorite language is {language.title()}")
#
#
# # We can also use the keys() method to loop through the keys rather than the key and the value.
#
# for name in favorite_languages.keys():
#     print(name.title())

# Looping through the keys is the default behavior, so we get the same result wether we use:

# for name in favorite_languages:
#
# or
#
# for name in favorite_languages.keys():

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

# Looping through the keys in a particular order.

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")


# We can also use the keys() method to see if a particular person was polled.

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

# We can also use the values() method to return a list of values without any keys.

print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()):
    print(language.title())

# This approach pulls all the values from the dictionary without checking for repeats.
# If we had a large poll we could end up with lots of repeated entries.
# To see each without repetition we can use a set.

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")

# To clarify when we wrap a set() around a list containing duplicate items, Pyhon identifies the unique items in the
# list and builds a set from those items

# Note: You can build a set directly using braces and separating the elements with commas.

# Example:
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
