prompt = "Welcome to Jiez's Pizza!"
prompt += "\nPlease enter toppings you wish to add (enter 'quit' to exit)\n"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("Your pizza is preparing...")
    else:
        print("We'll add the topping to your pizza...\n")