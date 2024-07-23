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


# number_of_guesses = 0
#
# score = 0

# Check if the user is correct
def compare(guess, highest):
    if guess == highest:
        guess_correct = True
        print("That's correct")
    else:
        guess_correct = False
        print("Sorry that's wrong")
    return guess_correct


#
# def track_score():

def get_followers(option_a, option_b):
    if option_a['follower_count'] > option_b['follower_count']:
        print("A has the larger follower count")
        highest = 'A'
    else:
        print("B has the larger follower count")
        highest = 'B'
    return highest


def game():
    # Print logo.
    print(logo)
    # Get random options from the data file.
    option_a = random.choice(data)
    option_b = random.choice(data)
    print(f"Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a['country']}")
    # Print second part of the logo.
    print(vs)
    print(f"Against B: {option_b["name"]}, a {option_b["description"]}, from {option_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    compare(guess, get_followers(option_a, option_b))
    while guess_correct:
        if guess == 'A':
            option_a = option_a
        else


game()
