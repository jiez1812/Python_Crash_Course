# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Print frist three players
print(players[0:3])
#Slice at index 1 and end at index 4
print(players[1:4])
# Slice at the beginning of the list
print(players[:4])
# Python return all items from the third item through the end of the list
print(players[2:])
# Print last three players would continue to work as the list of players changes in size
print(players[-3:])

#Looping through a site
# Loop through fist three players and print their names
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())