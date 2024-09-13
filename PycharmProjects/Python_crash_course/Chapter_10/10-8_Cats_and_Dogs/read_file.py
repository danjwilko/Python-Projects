files = ["cats.txt", "dogs.txt"]

for file_name in files:
    print(f"\nReading file: {file_name}:")
    try:
        with open(file_name) as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"File {file_name} not found.")

