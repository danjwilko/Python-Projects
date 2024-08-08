""" Using a for loop to view everything within the dictionary using the assigned key, value pairs. """

user_0 = {
    'username': 'efermi',
    'first:': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
