file = "learning_python.txt"

with open(file) as fileToRead:
    lines = fileToRead.readlines()

for line in lines:
    message = line.strip()
    modified = message.replace('Python', 'C')
    print(modified)