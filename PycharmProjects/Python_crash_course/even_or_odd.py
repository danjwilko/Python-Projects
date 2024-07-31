# Using the modulo operator.

number = input("Enter a number, and I'll tell you if its even or odd: ")
number = int(number)

# Even numbers are always divisible by 2. Modulo gives us the remainder, so where we modulo by two if the reminder is
# zero its even else its odd number

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

