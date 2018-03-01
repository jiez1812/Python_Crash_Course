class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("{0} is human.".format(self.first_name.title()))

    def greet_user(self):
        print("Hi, {0} {1}. Have a nice day.".format(self.first_name.title(), self.last_name.title()))

user_1 = User('john', 'walton')
user_2 = User('victoria', 'koch')
user_3 = User('camilia', 'mars')

user_1.describe_user()
user_1.greet_user()
print()

user_2.describe_user()
user_2.greet_user()
print()

user_3.describe_user()
user_3.greet_user()
print()