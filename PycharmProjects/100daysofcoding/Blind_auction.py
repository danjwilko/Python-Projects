from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.

print(logo)
bids = {}

bidding_finished = False
while not bidding_finished:
    bidder_name = input("What is your name? ")
    bid_price = int(input("What is your bid? "))

    should_continue = input("Are there any more bidders? type 'yes' or 'no'.")
    if should_continue.lower() == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()

