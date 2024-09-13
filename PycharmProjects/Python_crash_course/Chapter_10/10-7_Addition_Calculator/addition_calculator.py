next_sum = True

while next_sum:
    print("Enter the first number: ")
    first_number = input()
    print("Enter the second number: ")
    second_number = input()
    try:
        result = int(first_number) + int(second_number)
        print(f"{first_number} + {second_number} = {result}")
    except ValueError:
        print("One of the numbers entered is not an integer.")
    print("Do you want to do another sum? type y/n: ")
    if input() != 'y':
        next_sum = False


