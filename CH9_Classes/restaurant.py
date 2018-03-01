# Exercise 9-1

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0} make {1} foods.".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("{} is opens.".format(self.restaurant_name))

restaurant_1 = Restaurant('food book', 'western')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()