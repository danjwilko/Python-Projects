# from pathlib import Path
#
# path = Path('pi_digits.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
#
# print(pi_string)
# print(len(pi_string))

from pathlib import Path

# Note using the '..' notation tells python to look back one directory.
path = Path('..')/'pi_million_digits.txt'
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))