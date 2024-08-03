prompt = "Please enter a pizza topping you would like to add: "
prompt += "\nEnter 'quit' when you have finished. "

while True:
    topping = input(prompt)
    if topping != "quit":
        print(f"I'll add {topping} to your pizza toppings.")
    else:
        break
