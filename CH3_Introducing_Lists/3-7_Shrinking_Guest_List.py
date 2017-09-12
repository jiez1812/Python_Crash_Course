# Create a guest list who will be invited to dinned
guests = ["Eric", "Alex", "Sandra", "Edward", "Mozilla"]
print("\nFirst Invitation\n")
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
print("\nSecond Invitation\n")
print("Hi " + guests[0] + ", you are invited to dinner.")
print("Hi " + guests[1] + ", you are invited to dinner.")
print("Hi " + guests[2] + ", you are invited to dinner.")
print("Hi " + guests[3] + ", you are invited to dinner.")
print("Hi " + guests[4] + ", you are invited to dinner.")

# Insert more guests
guests.insert(0, "Ken")
guests.insert(4, "Jane")
guests.append("Neo")

# Print new invitation list
print("\nThird Invitation\n")
print("Hi " + guests[0] + ", you are invited to dinner.")
print("Hi " + guests[1] + ", you are invited to dinner.")
print("Hi " + guests[2] + ", you are invited to dinner.")
print("Hi " + guests[3] + ", you are invited to dinner.")
print("Hi " + guests[4] + ", you are invited to dinner.")
print("Hi " + guests[5] + ", you are invited to dinner.")
print("Hi " + guests[6] + ", you are invited to dinner.")
print("Hi " + guests[7] + ", you are invited to dinner.")

# Remove guests from list by using pop() method
print("\nRemove guest from list until two guests")
print("Hi " + guests.pop() + ", I'm sorry that I can't invite you to dinner")
print("Hi " + guests.pop() + ", I'm sorry that I can't invite you to dinner")
print("Hi " + guests.pop() + ", I'm sorry that I can't invite you to dinner")
print("Hi " + guests.pop() + ", I'm sorry that I can't invite you to dinner")
print("Hi " + guests.pop() + ", I'm sorry that I can't invite you to dinner")
print("Hi " + guests.pop() + ", I'm sorry that I can't invite you to dinner")

# Print message to each of the two people still on list.
print("\nMessages to two guests left")
print("Hi " + guests[0] + ", you are still invited to dinner.")
print("Hi " + guests[1] + ", you are still invited to dinner.")

# Delete last two guest by using del()
del guests[0]
del guests[0]

# Print empty guest list
print(guests)