#Slices
countries = ['Italy','France','Germany', 'Japan','Switzerland','Scotland', 'England','Spain']

print('The first three items in the list are:')
print(countries[:-3])

print('The items in the middle of the list are:')
print(countries[3:5])

print('The last three items in the list are:')
print(countries[-3:])

# My pizzas, your pizzas.
pizzas = ['hawaiian', 'ham and pineapple', 'donna special', 'meat feast']
friends_pizza = pizzas[:]

pizzas.append('cheese and tomato')
friends_pizza.append('pepperoni')

print('My favorite pizzas are:')
print(pizzas)

print('My friends favorite pizzas: ')
print(friends_pizza)

for pizza in pizzas:
    print(pizza)




