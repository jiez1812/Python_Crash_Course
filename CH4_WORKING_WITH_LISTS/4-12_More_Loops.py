# Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

# Add a new food to each list to prove we actually have 2 seperate lists
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for my_food in my_foods:
    print("\t" + my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print("\t" + friend_food)