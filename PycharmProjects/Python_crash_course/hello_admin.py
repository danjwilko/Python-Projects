# Hello admin

names = ['dan', 'rich', 'amy', 'david', 'rachel', 'admin']
if names:
    for name in names:
        if name == 'admin':
            print(f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again.")
# Adding an empty users list statement.
else:
    print("We need to find some users!")

