class Restaurant():
    """A simple Restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, is open!")



restaurant = Restaurant("Tarantino's", "italian")
restaurant.describe_restaurant()

restaurant = Restaurant("Golden Mill", 'chinese')
restaurant.describe_restaurant()
restaurant = Restaurant("Suttons", 'fish and chips')
restaurant.describe_restaurant()
restaurant = Restaurant("Pizza hut", 'pizza')
restaurant.describe_restaurant()

