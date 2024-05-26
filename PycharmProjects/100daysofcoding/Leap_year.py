# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# divisible by 4 evenly.
if (year % 4) == 0:
    result = "Leap year."
    # unless also divisible evenly by 100.
elif year % 100:
    result = "Not leap year."
    # Unless divisible by 400 evenly.
elif year % 400:
    result = "Leap year."
    # if not divisible by 4 evenly then.
else:
    result = "Not leap year."
print(result)
