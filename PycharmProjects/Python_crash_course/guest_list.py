guests = ['Bob', ' Rachel', 'Mike', 'Lisa']

print(f"Dear {guests[0]} you are invited to dinner")
print(f"Dear {guests[1]} you are invited to dinner")
print(f"Dear {guests[2]} you are invited to dinner")
print(f"Dear {guests[3]} you are invited to dinner")

print(f"Unfortunatly {guests[2]} cannot make it.")
guests[2] = "Shannon"
print(f"Dear {guests[0]} you are invited to dinner")
print(f"Dear {guests[1]} you are invited to dinner")
print(f"Dear {guests[2]} you are invited to dinner")

print(f"Dear {guests[3]} you are invited to dinner")

print(f"Hi {guests[0]} we have now got a larger table so are able to invite more people")
print(f"Hi {guests[1]} we have now got a larger table so are able to invite more people")
print(f"Hi {guests[2]} we have now got a larger table so are able to invite more people")
print(f"Hi {guests[3]} we have now got a larger table so are able to invite more people")

guests.insert(0, 'Richard')
guests.insert(2, 'Donna')
guests.append('Tina')

print(guests)

revoke_invite = guests.pop()
message = "Sorry but the table wont arrive in time so I can only invite 2 people. you wont be able to come"
print(f"{revoke_invite} {message}")
revoke_invite = guests.pop()
print(f"{revoke_invite} {message}")
revoke_invite = guests.pop()
print(f"{revoke_invite} {message}")
revoke_invite = guests.pop()
print(f"{revoke_invite} {message}")
revoke_invite = guests.pop()
print(f"{revoke_invite} {message}")

del(guests[1])
print(guests)
del(guests[0])
print(guests)