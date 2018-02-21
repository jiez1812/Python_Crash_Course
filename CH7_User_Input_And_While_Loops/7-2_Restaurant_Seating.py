prompt = "Welcome! How many people?"
prompt += "\nAns: "
num = input(prompt)
num = int(num)

if num > 8:
    print("\nSorry. You'll have to wait for a table.")
else:
    print("\nYour table is ready.")