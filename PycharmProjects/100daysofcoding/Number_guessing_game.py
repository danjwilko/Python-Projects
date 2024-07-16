# Number guessing game objectives

# Include ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100
# Check user's guess against actual answer. Print "Too high." or "To low". depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 in the hard mode).
import random

logo = """

 _____ _     _____ ____  ____    _____  _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __\/ \ /|/  __/  / \  /|/ \ /\/ \__/|/  _ \/  __//  __\
| |  _| | |||  \  |    \|    \    / \  | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | |  | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/  \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\
                                                                                           

"""

chosen_number = random.randint(1, 100)
guessed_numbers = []
guesses = 0


def clues(guess):
    if guess > chosen_number:
        return "Too high!"
    else:
        return "Too low!"


def make_guess(guesses, guessed_numbers):
    # number of guesses made
    guesses = guesses + 1
    # Lives remaining
    lives_remaining = lives - guesses

    # While user has lives remaining.
    while lives_remaining != 0:
        guess = int(input("Make your guess: "))
        if guess in guessed_numbers:
            print('You have already guessed that number')
        elif guess not in guessed_numbers and guess != chosen_number:
            guessed_numbers.append(guess)
            print(guessed_numbers)
            print(f"{clues(guess)}")
            print(f"You have {lives_remaining} attempts to guess the number.")
            print("Guess again.")
            make_guess(guesses, guessed_numbers)

        else:
            if guess == chosen_number:
                print(f"Congrats! You guessed the number in {guesses} guesses!")
    if lives_remaining == 0:
        print(f"You have {guesses} guesses left.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
if difficulty == "easy":
    lives = 10
if difficulty == "hard":
    lives = 5
make_guess(guesses, guessed_numbers)
