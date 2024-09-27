# from pathlib import Path
#
# path = Path('pi_digits.txt')
# contents = path.read_text()
# print(contents)

# from pathlib import Path
#
# path = Path('pi_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

# We can use the splitlines() method to turn a long string into a set of lines.
from pathlib import Path

path = Path('pi_digits.txt')
lines = path.read_text().splitlines()
for line in lines:
    print(line)

# Working with a files contents.

