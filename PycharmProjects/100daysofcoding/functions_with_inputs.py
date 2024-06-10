"""def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet() """


# Function that allows for input
# def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")


# greet_with_name("Angela")

def greet_with(name: "Angela", location: "London"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# keyword vs positional.
greet_with(name="Angela", location="London")
