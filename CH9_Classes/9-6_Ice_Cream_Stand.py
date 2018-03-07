# Exercise 9-6

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

    def increment_number_served(self, add_number):
        self.number_served += add_number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine):
        super().__init__(restaurant_name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'green apple', 'tiramisu', 'lemon']

    def describe_flavors(self):
        print("Ice Cream Flavors :")
        for flavor in self.flavors:
            print("\t- {}".format(flavor.title()))

my_stand = IceCreamStand('Ice House', 'Ice Cream')
my_stand.describe_restaurant()
my_stand.describe_flavors()