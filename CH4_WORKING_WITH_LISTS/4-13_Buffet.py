foods = ("burger", "noodles", "rice", "soup", "vege")

print("Food Menu:")
for food in foods:
    print("\t" + food)

# TypeError: 'tuple' object does not support item assignment
#foods[0] = "bread"

foods = ("bread", "noodles", "rice", "mushroom soup", "vege")

print("\nNew Food Menu:")
for food in foods:
    print("\t" + food)