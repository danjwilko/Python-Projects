# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S":
    sub_total = 15
elif size == "M":
    sub_total = 20
else:
    sub_total = 25

if add_pepperoni == "Y":
    if size == "S":
        sub_total += 2
    else:
        sub_total += 3

if extra_cheese == "Y":
    sub_total += 1

print(f"Your final bill is: ${sub_total}.")


