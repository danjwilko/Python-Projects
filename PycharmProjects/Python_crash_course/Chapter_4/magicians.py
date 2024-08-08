# Loops
# We can use a loop to perform the same action on each item within a list.
magicians = ['alice', 'david', 'carolina']
# The colon at the end of the statment tells python to interpret the next line as the start of the for loop.
for magician in magicians:
    # Always indent the line after a for loop statement.
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick,{magician.title()}.\n")

# Doing something after the loop.

print("Thank you everyone. That was a great magic show!")



