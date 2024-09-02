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



