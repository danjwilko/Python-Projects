# Using variables in strings.

first_name = "ada"
last_name = "lovelace"

# these strings are called f-strings, the f is for format.
full_name = f"{first_name} {last_name}"
# print(full_name)

#print(f" Hello, {full_name.title()}")

# these can also be used as a variable.

message  = f" Hello, {full_name.title()}"

print(message)
