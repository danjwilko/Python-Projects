############DEBUGGING#####################

# # Describe Problem
#
# """This function is supposed to run through the numbers 1-20 and
# when it reaches 20, it should print the statement"""


# def my_function():
#     # We actually never reach 20.So we need to change 20- 21.
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # When selecting using index we start at 0, so by having th range 1-6 were actually looking for index 2-7.
# # changing randint(1,6) to 0-5 we cover the index values.
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# # year 1994
# year = int(input("What's your year of birth?"))
# # when entering th year 1994 nothing happens, that's because we have nothing to catch that year and evaluate it.
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")


# Fix the Errors This takes an input but the input is a string so we get a type error. we have to add type int(input(
# )) to the input to specify the type of variable.
# The string output is also missing the f to denote a f-string.

# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# Print is Your Friend The error here is the error
# with the syntax == instead of =.

# # pages = 0
# # word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
