# The if-elif-else Chain
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

# Version 2: Just set price inside the if-elif-else block
# Then print statement that runs after the chain has been evaluated.

age = 12

if age <= 4:
    price = 0
elif age < 18:
    price = 5
# Multiple elif Blocks
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")