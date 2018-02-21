prompt = "Please enter a number to check whether it is a multiple of 10."
prompt += "\nInput: "

num = input(prompt)
num = int(num)

if num % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The numbe is not multiple of 10.")