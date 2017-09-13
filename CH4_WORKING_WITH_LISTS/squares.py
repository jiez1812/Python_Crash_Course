#Generate list of square of each integer

## Method 1
squares = []
for value in range(1, 11):
    square = value**2
    squares.append((square))

print(squares)

# Resetting
print("="*12 + " Resetting " + "="*12)
del squares
del square

# Method 2
squares = []
for value in range(1, 11):
    squares.append((value**2))

print(squares)

# Resetting
print("="*12 + " Resetting " + "="*12)
del squares

# Method 3
squares = [value**2 for value in range(1,11)]
print(squares)