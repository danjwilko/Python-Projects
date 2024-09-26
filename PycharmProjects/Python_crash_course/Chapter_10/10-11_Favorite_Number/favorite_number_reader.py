import json

filename = 'favorite_number.json'
with open(filename) as f:
    fav_num = json.load(f)

print(fav_num)