# Checking Usernames

current_users = ['dan', 'Rich', 'amy', 'david', 'rachel', 'admin']

new_users = ['jeremy', 'lucy', 'rich', 'steve', 'abigail', 'emma', 'amy,']

current_user_lookup = {name.lower() for name in current_users}
for name in new_users:
    if name.lower() in current_user_lookup:
        print(f"Sorry {name} is already taken, you will need to input a new username")
    else:
        print("The username is available")

