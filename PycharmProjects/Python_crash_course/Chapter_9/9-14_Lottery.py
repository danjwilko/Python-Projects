from random import choice

nums_letters = ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chosen_list = []
for num in range(4):
    chosen = choice(nums_letters)
    chosen_list.append(chosen)
print(f"Any ticket that matches: {chosen_list} wins a prize.")
