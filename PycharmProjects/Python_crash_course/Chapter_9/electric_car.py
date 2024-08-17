# Inheritance
# If the class you are writing is a specialised version of another class you have written, we can use inheritance.
# When one class inherits from another, it takes on the attributes and methods of the first class.
# The original class is the parent class, and the new class is the child class.


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialise the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car has a {range} miles on full charge")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    # Defining Attributes and Methods for the child class.
    # Once we have a child class that inherits from a parent class, you can add any attributes and methods necessary to
    # differentiate the child class from the parent class.

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# There's no limit to how much we specialise the ElectricCar class. You can add as many attributes and methods
# as we need to model an electric car to whatever degree of accuracy we need.
# An attribute or method that could belong to any car, rather than one that's specific to an electric car, should be
# added to the Car class instead of the ElectricCar class.

# Overriding Methods from the parent class.

# You can override any method from the parent class that doesn't fit what your trying to model with the child class.
# To do this, we define a method in the child class with the same name as the method you want to override in the parent
# class.
# Python will disregard the parent class method and only pay attention to the method you defined in the child class.

# Instances as Attributes.

# When modelling something from the real world in code, you may find that you're adding more and more details to
# a class.
# You'll find that you have a growing list of attributes and methods, and the files are becoming lengthy.
# We might recognise at this point that part of one class can be written as a separate class.
# We have modified the ElectricCar class above and moved the battery details to its own class.

# Modelling Real-World Objects.
# As we begin to model more complicated things like electric cars, you'll wrestle with interesting questions.
# Is the range of an electric car a property of the battery or the car?
# If were only describing one car, it's probably fine to maintain the association of the method get_range() with the
# battery class.
# But if were describing an entire manufacturer's entire line of cars, we probably want to move get_range() to the
# ElectricCar class.

