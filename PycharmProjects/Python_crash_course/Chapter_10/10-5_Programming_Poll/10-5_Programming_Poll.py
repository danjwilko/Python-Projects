file_name = "poll_results.txt"

responses = []

while True:
    reason = input("\nWhy do you like programming: ")
    responses.append(reason)

    add_person = input("Do you want to add another ? Type y/n: ")
    if add_person != 'y':
        break

with open(file_name, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
