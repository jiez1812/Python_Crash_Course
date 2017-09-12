# Create a guest list who will be invited to dinned
guests = ["Eric", "Alex", "Sandra", "Edward", "Mozilla"]
print("Hi " + guests[0] + ", you are invited to dinner.")
print("Hi " + guests[1] + ", you are invited to dinner.")
print("Hi " + guests[2] + ", you are invited to dinner.")
print("Hi " + guests[3] + ", you are invited to dinner.")
print("Hi " + guests[4] + ", you are invited to dinner.")

# Print the name of guest who can't make the dinner
print("\n" + guests[2] + " can't make the dinner. Please replace to another guest.\n")

# Replace new guests
guests[2] = "Monica"

# New invitation list
print("Hi " + guests[0] + ", you are invited to dinner.")
print("Hi " + guests[1] + ", you are invited to dinner.")
print("Hi " + guests[2] + ", you are invited to dinner.")
print("Hi " + guests[3] + ", you are invited to dinner.")
print("Hi " + guests[4] + ", you are invited to dinner.")