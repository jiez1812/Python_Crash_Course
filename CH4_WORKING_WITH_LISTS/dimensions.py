# Defining a Tuple
dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

# Looping through all values in a tuple
print("Original dimension:")
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
print("\nModified dimension")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)