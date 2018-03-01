class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0} make {1} foods.".format(self.restaurant_name.title(), self.cuisine_type))

    def open_restaurant(self):
        print("{} is opens.".format(self.restaurant_name.title()))

restaurant_1 = Restaurant('naruto restaurant', 'Naruto themes')
restaurant_2 = Restaurant('alaska', 'france')
restaurant_3 = Restaurant('xian jian', 'chinese')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()