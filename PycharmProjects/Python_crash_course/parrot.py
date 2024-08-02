""" Using the input() function to use the user's input."""

# The input() function takes one argument : the prompt or instruction we want to display to the user.
prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)
#
# # This prints the 'quit' input, so we need to fix this.
#     if message != 'quit':
#         print(message)

"""Using Flags to signal to the program"""

# set the flag to True starts and continues the while loop.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        # The Message is 'quit' so the flag is set to False
        active = False

    else:
        # The message is not equal to 'quit' so the message is printed and we start the loop again.
        print(message)

