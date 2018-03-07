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

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin's privileges: ")
        for privilege in self.privileges:
            print("\t- {}".format(privilege))

new_admin = Admin('God', 'Like')
new_admin.greet_user()
new_admin.show_privileges()