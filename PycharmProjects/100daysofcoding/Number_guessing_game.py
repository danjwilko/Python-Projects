# Number guessing game objectives

# Include ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100
# Check user's guess against actual answer. Print "Too high." or "To low". depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 in the hard mode).
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

logo = """

 _____ _     _____ ____  ____    _____  _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __\/ \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\
| |  _| | |||  \  |    \|    \    / \  | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | |  | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/  \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\
                                                                                           

"""


# function to check users guess against the chosen random number

def check_guess(user_guess, chosen, turns):
    """checks answer against chosen number and remaining turns"""
    if user_guess > chosen:
        print("Too high.")
        return turns - 1
    elif user_guess < chosen:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {chosen}.")


# Make a function to set the difficulty

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choose a number at random between 1 and 100
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    chosen = randint(1, 100)
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    # repeat the guessing function if they get it wrong
    user_guess = 0
    while user_guess != chosen:
        # let the user guess a number
        user_guess = int(input("Make a guess: "))
        check_guess(user_guess, chosen, turns)


# Track the number of turns and reduce by 1 if they get the guess wrong.


game()
