class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over")

# Line 1 we define a class called Dog#
# Line 2 we write a docstring describing what the class does.

# Line 4: The __init__() method is a special method that Python runs automatically, whenever we create a new instance
# based on the dog class.
# The self-parameter is required in the method definition, and it must be before the other parameters.

# The two variables defined at line 6 each have the self prefix. Any variable prefixed with self is available to every
# method in the class, and well also be able to access these variables through any instance created from the class.

# Making an instance from a class

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old ")

# Calling methods.

# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

# To call a method, give the name of the instance and the method you want to call, seperated by a dot. When Python
# reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code.

# Creating Multiple Instances,
# You can create as many instances from a class as you need.

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy',)

