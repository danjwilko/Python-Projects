from HL_game_data import data
import random


def format_data(account):
    """Format the account data into printable form"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return account_name, account_desc, account_country


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art.
score = 0
# print(logo)


game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    """ Generate a random account."""
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    # print logo vs

    print(f"Against B: {format_data(account_b)}")

    # Ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen.
    # If we were using the replit it would clear, doesnt in console for some reason
    # clear()
    # print(logo)

    # Give user feedback on guesses.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


