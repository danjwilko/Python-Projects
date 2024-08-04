"""Program that polls users on their dream holiday"""

dream_holidays = {}

# Flag for polling active.

poll_active = True

while poll_active:
    # Prompt users for a response.
    name = input('What is your name? ')
    destination = input('What is your dream holiday destination? ')

    # Storing the users response in the dictionary.
    dream_holidays[name] = destination

    next_person = input("Would anyone else like to add their dream holiday? (yes/ no) ")
    if next_person == 'no':
        poll_active = False

# Poll complete.

print("\n**** Dream Holiday Results ****")
for name, destination in dream_holidays.items():
    print(f"{name}'s dream holiday destination is: {destination.title()}")
