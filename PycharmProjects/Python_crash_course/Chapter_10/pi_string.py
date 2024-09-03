# Making a list of lines from a file

# When you use with, the file object returned by open() is only available inside the block that contains it.
# If we want to retain access to a files contents, you can store the files lines in a list inside the block
# then work with that list.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Working with a files contents

# After we've read a file into memory, you can do whatever you want with the data. Here we will attempt to build a
# single string containing all the digits in the file with no whitespace between.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# Ouptut:
# 3.14159265535   8979323846   2643383279
# 39

# We still have the whitespace that is on the left side of the digits that was on each line, we can remove this by
# using strip() rather instead of rstrip()

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Large files: One Million Digits.
# We can work with larger files, for example, rather than using 30 decimal places, we can use pi to 1,000,000 decimal
# places, without altering the code, we simply pass in a new file. well also limit the output to 50 decimal places.

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is you birthday contained in py.


filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


birthday = input("Enter your birthday in the form ddmmyy:")
if birthday in pi_string:
    print(f"Your birthday appears in the first million digits of pi!")
else:
    print(f"Your birthday does not appear in the first million digits of pi!")


