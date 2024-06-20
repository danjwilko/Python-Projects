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


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder.capitalize()
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    bidder_name = input("What is your name?: ")
    bid_price = int(input("What is your bid?: $"))
    bids[bidder_name] = bid_price
    should_continue = input("Are there any more bidders? type 'yes' or 'no'.")
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
