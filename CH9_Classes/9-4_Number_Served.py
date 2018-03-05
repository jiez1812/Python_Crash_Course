# Exercise 9-1

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("{0} make {1} foods.".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("{} is opens.".format(self.restaurant_name))

    def print_number(self):
        print("Customer served : {}".format(self.number_served))

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self):
        self.number_served += 1

restaurant_1 = Restaurant('food book', 'western')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.print_number()

# Change serve number
restaurant_1.number_served = 10
restaurant_1.print_number()

restaurant_1.set_number_served(1)
restaurant_1.print_number()

restaurant_1.increment_number_served()
restaurant_1.print_number()