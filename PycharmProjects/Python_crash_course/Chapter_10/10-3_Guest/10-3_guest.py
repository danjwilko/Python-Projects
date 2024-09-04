filename = 'guest.txt'

name = input('What is your name? ')
with open(filename, 'w') as file_to_write:
    file_to_write.write(name)
    