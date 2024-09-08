def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = "alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"
for filename in filenames:
    count_words(filename)


# Filing silently:
# In the previous example we informed our users that one of the files was unavailable. But we dont have to every time.
# sometimes you will want the program to fail silently when an exception occurs.
# To fail silently we write a try block as normal however we tell Python to do nothing in the except block.

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = "alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"
for filename in filenames:
    count_words(filename)