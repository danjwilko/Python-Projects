sandwich_orders = ['bacon', 'bacon and egg', 'jam', 'club', ' cheese and tomato']

finished_sandwiches = []

# Printing a message to say the sandwich has been made.
# Removing the sandwich from the order list.
# Adding the sandwich to the finished list.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I've made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

# Print all the completed sandwiches.
print(finished_sandwiches)
