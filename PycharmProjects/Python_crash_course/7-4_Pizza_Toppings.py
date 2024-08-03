prompt = input("Please enter a pizza topping you would like to add: ")
prompt += "\nEnter 'quit' when you have finished "

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
