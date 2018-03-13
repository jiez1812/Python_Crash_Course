filename = 'guest_book.txt'

active = True
with open(filename, 'w') as file_object:
    while active:
        message = "Please enter a guest's name.\n"
        message += "Input 'end' to stop.: "

        guestname = input(message)
        if guestname.lower() != "end":
            file_object.write(guestname + "\n")
        else:
            active = False