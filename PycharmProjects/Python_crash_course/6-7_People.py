# Person

person1 = {'first_name': 'ava', 'last_name': 'smith', 'age': 6, 'city': 'skegness'}
person2 = {'first_name': 'ariella', 'last_name': 'smith', 'age': 3, 'city': 'skegness'}
person3 = {'first_name': 'yaz', 'last_name': 'smith', 'age': 33, 'city': 'skegness'}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}, is {person['age']} years old from"
          f" {person['city'].title()}")







