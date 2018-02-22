prompt = "Welcome to Jiez's Pizza!"
prompt += "\nPlease enter toppings you wish to add (enter 'quit' to exit)\n"

while True:
    message = input(prompt)

    if message == 'quit':
        print("Your pizza is preparing...")
        break
    else:
        print("We'll add the topping to your pizza...\n")