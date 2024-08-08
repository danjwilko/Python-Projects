# Favorite numbers

favorite_numbers = {
    'yasmine': [5, 10],
    'ava': [6,],
    'daniel': [14,],
    'sam': [44, 12],
    'rich': [66, 10],
    }

for name, numbers in favorite_numbers.items():
    print(f'\n{name}:')
    for number in numbers:
        print(f'\t{number}')


