# Working with Classes and instances.
# You can use classes to represent many real-world situations. Once you write a class,
# you'll spend most of your time working with instances created from the class.
# One of the first tasks you'll want to do is modify the attributes associated with a particular instance.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('Audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())


# Setting a Default Value for an attribute.

# When an instance is created, attributes can be defined without being passed in as parameters.
# These attributes can be defined in the __init__() method where they are assigned a default value.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Adding in a attribute that always start with 0.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('Audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying the Attribute Values
# We can change the attribute's value in three ways, directly through the instance, set through a method
# or increment the value through a method.

# Modifying directly.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Modifying through a method.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer back!")


my_new_car = Car('Audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.update_odometer(100)
my_used_car.read_odometer()


