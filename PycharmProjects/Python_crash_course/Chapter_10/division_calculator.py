# Python uses special objects called exceptions to manage errors that arise during a program's execution.
# Whenever an error occurs that makes Python unsure what to do next, it creates an exception object.
# If you create code that handles the exception, the program will continue running, if you dont handle the exception
# the program will halt and show a traceback.

#Handling the ZeroDivisionError Exception

#print(5/0)

# It's impossible to divide by zero, but we have asked python to do it anyway. here we get
# a traceback as Python can't do this. In the example Python has stopped the program and given us the kind of exception
# raised we can use this to modify the program, so we can tell python what to do with this type of exception occurs.

# Using try-except Blocks

# When you think an error may occur we can write a try-except block to handle the exception that might be raised.

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

# We know the division by zero will produce the exception so we will get the message "You can't divide by zero".
# However, if the code in the try block worked Python would skip the except block.

# Using Exceptions to Prevent crashes.

# Handling errors correctly is important when the program has more work to do after the error occurs.
# This happens often in programs that prompt users for input. If the program responds to invalid input appropriately, it
# can prompt for more valid input.
# Example with no exception handling:

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)
#
# Example with exception handling:
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)



