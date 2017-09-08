# Changing, Adding, and Removing Elements
# Modifying Elements in a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Adding Elements to a List
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Append elements in an empty list
motorcycles = []
print(motorcycles)

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Removing Elements from a List
# Removing an Item Using the del Statement
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Removing an Item using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Popping items from any Position in a list
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Removing an Item by Value
motorcycles = ['honda', 'yamada', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("\n" + "#"*10 + " Resetting " + "#"*10 + "\n")

# Use the remove() method to work with a value that's being removed from a list.
motorcycles = ['honda', 'yamada', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")