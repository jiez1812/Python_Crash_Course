# Checking for Inequality, !=
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

# Resetting
del requested_topping

# Testing Multiple Conditions
# Use a series of simple if statements

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")

print("\nFinished making your pizza!")