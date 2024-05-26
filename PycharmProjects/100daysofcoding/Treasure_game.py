print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

user_choice = input(
    "You have just disembarked from the boat that brought you here, as you stand on the jetty, you see you can either "
    "go left towards the beach or go right towards a cave in the cliff face. Type 'left' for the beach or 'right' for "
    "the cave.")
choice = user_choice.lower()

if choice == "left":
    print("You chose to go left towards the beach")
    print(
        "As you walk along the beach, you come to a river mouth. \n There is a boat tied up nearby, you could use "
        "this to go upstream, as you look upstream you see a small rickety bridge that crosses to the other side ")
    choice = input(
        "Do you take the boat upstream or cross the rickety bridge? Type 'boat' to take the boat, or type bridge to "
        "cross the bridge.")
    if choice == "boat":
        print("As you climb into the boat and cast off, you notice there is no oars, you drift out to sea")
        print("Game over")
    else:
        print("You cross the rickety bridge, surprised it didnt fall to peices.")
        print("You follow a path on the other side of the river to a clearing")
        print("The clearing has several boulders marked with some strange markings, that are different colours, blue, "
              "gold, black. It looks like there is something underneath each boulder.")
        print("The boulders look like they can be moved.")
        choice = input("Which boulder do you choose to move? Type 'blue', 'gold' or 'black'.")
        if choice == "blue":
            print("You move the boulder with the blue markings, underneath is a wooden box.")
            print("You found the treasure")
            print("You win!")
        elif choice == "gold":
            print(
                "You chose the boulder with the gold markings.\n You move the boulder slowly.\n Oh no!, it triggered a "
                "trap door, you fall into the trap")
            print("Game over.")
        else:
            print(
                "You chose the black boulder, its a little bit bigger than the rest you realise, as you struggle to "
                "move it. \n Its starts to move finally but its rolling towards you, you cannot stop it.")
            print("The boulder squashes you.")
            print("Game over.")
else:
    print(
        "You chose to go to the cave. \n As you walk further into the cave the light begins to fade, you cannot see "
        "where you are going. You lose your footing and fall down a hole you cannot get out")
    print("Game over")
