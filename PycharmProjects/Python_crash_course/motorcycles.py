# Changing, adding, and removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

# using index values to modify specific items within the list.
#motorcycles[0] = 'ducati'

#print(motorcycles)

# Append - adds items to the end of the list.

motorcycles.append('ducati')

#print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')

#print(motorcycles)

# Inserting elements using insert method.

#motorcycles = ['honda', 'yamaha', 'suzuki']

#motorcycles.insert(0, 'ducati')
#print(motorcycles)

# removing elements
# If you know the position of the item, you can use del to remove the item from the list

# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

# If you want or need to use the item after removing from the list, you can use the pop method.
# the pop() method removes the last item, but lets you use it after removing. The term pop comes from the thinking
# of the list as a stack and removing the last item at the top of the stack.

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# pop method, prints the modified list and the item we just removed.
# except now we can use the item that was removed.
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}")


# Removing an item from any point in the list.
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}")

# removing an item by value.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

#motorcycles.remove('ducati')
#print(motorcycles)


# to_expensive = 'ducati'
# motorcycles.remove(to_expensive)

# print(f"\nA {to_expensive.title()} is to expensive for me.")

# To access items in a list the first item starts at 0 not a 1.
# to access the last item in a list regardless if the list has been modified, you can use the index -1
print(motorcycles[-1])

# If the list is empty and this method is used it will return an error.





