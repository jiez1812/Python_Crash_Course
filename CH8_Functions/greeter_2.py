# Passing Information to a Function

def greet_user(username):
    """Display a simple greeting"""
    print("Hello, {0}!".format(username.title()))

greet_user('jesse')