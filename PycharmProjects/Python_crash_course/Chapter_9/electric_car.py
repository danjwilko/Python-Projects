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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    # Defining Attributes and Methods for the child class.
    # Once we have a child class that inherits from a parent class, you can add any attributes and methods necessary to
    # differentiate the child class from the parent class.

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery}-kwh battery")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
