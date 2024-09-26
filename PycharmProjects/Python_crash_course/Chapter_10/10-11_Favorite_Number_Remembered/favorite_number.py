import json

# Load a users favorite number if it has been stored previously.
# Otherwise, prompt for the users favorite number.

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        users_fav_number = json.load(f)
except FileNotFoundError:
    users_fav_number = input("Please enter your favorite number: ")
    with open (filename, 'w') as f:
        json.dump(users_fav_number, f)
        print(f"We'll remember your favorite number {users_fav_number}")
else:
    print(f"Your favorite number is {users_fav_number}")


