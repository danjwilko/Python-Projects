import json

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    favorite_number = input('Enter favorite number: ')
    json.dump(favorite_number, f)
