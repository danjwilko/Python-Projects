# Using json.dump() and json.load()

"""Short program that stores a set of numbers and another program that reads these numbers back into memory"""
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
