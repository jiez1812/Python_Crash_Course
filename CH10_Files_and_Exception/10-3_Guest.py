filename = 'guest.txt'

guestname = input("Please enter guest's name: ")

with open(filename, 'w') as file_object:
    file_object.write(guestname + "\n")