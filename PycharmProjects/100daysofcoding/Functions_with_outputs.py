# Functions with outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("John", "Smith")
print(formatted_string)

# we could also put the function call inside the print.

print(format_name("John", "Smith"))

# function weve been using with an input and an output.
output = len("Daniel")
print(output)

