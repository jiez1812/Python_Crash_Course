class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("{0} is human.".format(self.first_name.title()))

    def greet_user(self):
        print("Hi, {0} {1}. Have a nice day.".format(self.first_name.title(), self.last_name.title()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

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

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)