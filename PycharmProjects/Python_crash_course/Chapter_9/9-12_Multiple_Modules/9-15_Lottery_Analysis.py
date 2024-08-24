from random import choice


def create_winning_ticket():
    winning_ticket = []
    while len(winning_ticket) < 4:
        chosen = choice(possible_char_nums)
        if chosen not in winning_ticket:
            winning_ticket.append(chosen)
    return winning_ticket


def create_ticket(possible_char_nums):
    ticket = []
    while len(ticket) < 4:
        chosen = choice(possible_char_nums)
        if chosen not in ticket:
            ticket.append(chosen)
    return ticket


def check_ticket(winning_ticket, ticket):
    for item in winning_ticket:
        if item not in ticket:
            return False
    return True


possible_char_nums = ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
winning_ticket = create_winning_ticket()

counter = 0
match = False

while not match:
    new_ticket = create_ticket(possible_char_nums)
    counter += 1
    match = check_ticket(winning_ticket, new_ticket)
    if match:
        print(f"Your ticket {new_ticket}, matches the winning ticket: {winning_ticket}. You win!")
        print(f"\tIt took {counter} runs of the loop to find a match.")

