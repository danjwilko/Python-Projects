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


restaurant = Restaurant("Tarantino's", "italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.get_number_served()
restaurant.increment_number_served(5)
restaurant.get_number_served()

