import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3:
    print("You chose an invalid number, you lose")
else:
    print(f"You chose {game_images[user_choice]}")
    comp_choice = random.randint(0, 2)
    print(f"Computer chose {game_images[comp_choice]}")

    if user_choice == comp_choice:
        print("Draw")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose")
    elif user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif user_choice < comp_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win!")
# Alternately I originally wrote out the statements for each choice, we had a few more lines of code, but it worked
# just the same.

