# Functions with outputs

def format_name(f_name, l_name):
    if f_name =="" or l_name=="":

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
        # if we put a print statement here it would not run as the return has told the program where the end is.

print(format_name(input("What is your first name?"), input("What is your last name?")))

