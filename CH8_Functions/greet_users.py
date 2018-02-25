def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, {0}!".format(name.title())
        print(msg)

usernames = ['hannah', 'ty', 'margit']
greet_users(usernames)