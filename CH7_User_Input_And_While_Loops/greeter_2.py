# You can store your prompt in variable and pass the variable to the input() function

prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, {0}!".format(name))