locations = ["London", "Beijing", "Tokyo", "New York", "Bangkok"]
print("Original List: ")
print(locations)

print("\nSorted List:")
print(sorted(locations))

print("\nOriginal List:")
print(locations)

print("\nReverse List with sorted():")
print(sorted(locations, reverse=True))

print("\nOriginal List:")
print(locations)

print("\nReverse List with reverse():")
locations.reverse()
print(locations)

print("\nReverse again to original order:")
locations.reverse()
print(locations)

print("\nSort List as alphabetical:")
locations.sort()
print(locations)

print("\nSort List as reverse alphabetica:")
locations.sort(reverse=True)
print(locations)