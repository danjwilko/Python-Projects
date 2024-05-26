#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total = float(input("What was the total bill?"))
tip_perc = int(input("What percentage would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

split = (total / people) * ((tip_perc / 100) + 1)
final_amount = "{:.2f}".format(split)
print(f"Each person should pay: ${final_amount}")