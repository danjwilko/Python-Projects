# Conditional tests

fruit = 'apple'

print("Is fruit == 'apple? I predict True")
print(fruit == 'apple')

string_0 = 'hello_world'
string_1 = 'hello_world'

if string_0 == string_1:
    print(True)
else:
    print(False)

car = 'Audi'
if car.lower() == 'audi':
    print(True)
else:
    print(False)

string_2 = 'AAAA'
string_3 = 'AABA'

if string_2 in string_3:
    print(True)
else:
    print(False)

if string_2 not in string_3:
    print(True)
else:
    print(False)
