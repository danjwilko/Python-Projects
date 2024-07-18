from HL_game_data import data
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Create two choices A and B

# Ask the user which is highest.

# Compare the response to the highest.
# Track number of right gueses

# Keep track of previous right answer.
# make the previous high/correct answer the new A comparison.

# Compare the two options and set the highest value.
highest = ''


def choice_a():
    a = random.choice(data)
    return a


def choice_b():
    b = random.choice(data)
    return b


def compare(first, second):
    a_followers = first.get("followers")
    b_followers = second.get("followers")
    print(a_followers)
    print(b_followers)
    if a_followers > b_followers:
        highest = 'a'
    else:
        highest = 'b'
    return highest


def compare_guess(response):
    if response.lower() == highest:
        print("correct")


def game():
    first = choice_a()
    second = choice_b()
    compare(first, second)
    print(logo)
    print(f"Compare A: {first.get("name")}, who is an {first.get("description")}, from {first.get("country")}.")
    print(vs)
    print(f"Against B: {second.get("name")}, who is an {second.get("description")} from {second.get("country")}.")
    response = input("Who has more followers? Type 'A' or 'B': ")
    compare_guess(response)


game()
