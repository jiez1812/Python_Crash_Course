countries = ["China", "Malaysia", "Singapore", "Japan", "Russia", "Australia"]
print("Print countries:")
print(countries)

print("\nPrint 3rd country:")
print(countries[2])

print("\nPrint with string:")
print("Living countries : " + countries[1])

print("\nChange element:")
countries[3] = "USA"
print(countries)

print("\nInsert Country in 3rd element:")
countries.insert(2, "Thailand")
print(countries)

print("\nInsert Country in last element:")
countries.append("France")
print(countries)

print("\nDelete last country:")
countries.pop()
print(countries)

print("\nDelete 1st country:")
del countries[0]
print(countries)

print("\nSorted Locations:")
print(sorted(countries))

print("\nReverse sorted locations:")
print(sorted(countries, reverse=True))

print("\nUse Reverse Function:")
countries.reverse()
print(countries)

print("\nUse sort():")
countries.sort()
print(countries)

print("\nUse reverse sort()")
countries.sort(reverse=True)
print(countries)

print("\nLength of List:")
print(len(countries))