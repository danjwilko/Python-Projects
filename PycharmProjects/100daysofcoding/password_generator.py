#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

for num in range(0, nr_letters + 1):
    i = random.randint(0, len(letters) - 1)
    char = letters[i]
    password = password + char

for num in range(0, nr_symbols + 1):
    i = random.randint(0, len(symbols) - 1)
    char = symbols[i]
    password = password + char
for num in range(0, nr_numbers + 1):
    i = random.randint(0, len(numbers) - 1)
    char = numbers[i]
    password = password + char

rand_password = ''
for num in range(0, len(password)):
    i = random.randint(0, len(password) - 1)
    char = password[i]
    rand_password = rand_password + char

print(rand_password)

# I didn't want to use choice() as in a previous lesson, were told not to use it so set a challenge.

# option 2 way of doing it

passwordl = []

for char in range(1, nr_letters + 1):
    passwordl.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    passwordl.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    passwordl.append(random.choice(symbols))

random.shuffle(passwordl)
ran_password = ''
for char in passwordl:
    ran_password = ran_password + char
print(f" Your password is: {ran_password}")




