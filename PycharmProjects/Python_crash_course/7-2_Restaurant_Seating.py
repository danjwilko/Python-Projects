booking = input("Please enter how many people require to be seated: ")
booking = int(booking)

if booking > 8:
    print("You will have to wait for a table to become available.")
else:
    print("Your table is ready.")
    