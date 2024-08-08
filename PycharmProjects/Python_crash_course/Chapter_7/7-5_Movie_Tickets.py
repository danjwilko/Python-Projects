user_age = " Enter your age: "
user_age += "\n Enter 'quit' to quit: "

while True:
    age = input(user_age)
    if age == "quit":
        break
    age = int(age)
    if age > 12:
        price = 15
    elif 3 <= age <= 12:
        price = 10
    elif age < 3:
        price = 0

    print(f'Your ticket price is ${price}')
