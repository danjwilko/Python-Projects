file = "learning_python.txt"

print("Reading the entire file and outputting the contents: \n")
with open(file) as fileToRead:
    contents = fileToRead.read()

print(contents)

file = "learning_python.txt"

print("Looping through the file object and outputting the contents: \n")
with open(file) as fileToRead:
    for line in fileToRead:
        print(line.rstrip())
    print("\n")

file = "learning_python.txt"

with open(file) as fileToRead:
    lines = fileToRead.readlines()

print("Storing the file lines in a list and outputting the contents: \n")
for line in lines:
    print(line.rstrip())


