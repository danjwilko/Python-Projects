# Writing clear prompts.
# A clear instruction to the user of what we want them to input.
# name = input("Please enter your name: ")
# print(f"\nHello, {name}")
# By adding the space at the end of the prompt, it gives a space between text and the user response

prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}")

