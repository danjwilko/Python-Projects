class Restaurant():
    """A simple Restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, is open!")

    def get_number_served(self):
        print(f"{self.restaurant_name.title()} has served {self.number_served} customers.")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers served."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """Represent an Ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """Initialise an Ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def show_flavours(self):
        """Show the flavours available"""
        print(f"We have the following flavors available: ")
        for flavour in self.flavours:
            print(f" - {flavour.title()}")


refreshing_ice = IceCreamStand("Refreshing Ice", "ice cream")
refreshing_ice.flavours = ["vanilla", 'strawberry', 'chocolate']
refreshing_ice.describe_restaurant()
refreshing_ice.open_restaurant()
refreshing_ice.get_number_served()
refreshing_ice.show_flavours()
