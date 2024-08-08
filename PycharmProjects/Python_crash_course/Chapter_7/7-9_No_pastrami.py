
# Sandwich orders to fulfil.
sandwich_orders = ['bacon', 'pastrami', 'bacon and egg', 'jam', 'bacon', 'pastrami', 'club',
                   'cheese and tomato', 'pastrami',]

# Empty list for holding completed orders.
finished_sandwiches = []

# Print message if were out of ingredients.
print("Unfortunately, we have run out of pastrami.")

# Looping through the list to remove item.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


# Printing a message to say the sandwich has been made.
# Removing the sandwich from the order list.
# Adding the sandwich to the finished list.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I've made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

# Print all the completed sandwiches.
print(finished_sandwiches)
