another_user = True
file_name = "guest_book.txt"

while another_user:
    name = input('Enter your name: ')
    print(f"Hello, {name}, thank you for visiting")
    with open(file_name, 'a') as f:
        f.write(f"{name}\n")
    add_guest = input("Do you want to add another guest? Type y/n: ")
    if add_guest == 'n':
        another_user = False
