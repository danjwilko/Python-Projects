line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
num = int(position[1])

if letter == 'a':
    col = 0
elif letter == 'b':
    col = 1
elif letter == 'c':
    col = 2

if num == 1:
    row = 0
elif num == 2:
    row = 1
elif num == 3:
    row = 2

map[row][col] = 'X'

'''
method used by Angela Wu

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[number_index][letter_index] = "X"

print(f"{line1\n{line2}\n{line3}")'''







# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")