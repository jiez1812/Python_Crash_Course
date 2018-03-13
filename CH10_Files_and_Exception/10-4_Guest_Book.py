def append_file(filename, guestname):
    with open(filename, 'a') as file_object:
        file_object.write(guestname + "\n")

filename = 'guest.txt'

active = True
while active:
    message = "Please enter a guest's name.\n"
    message += "Input 'end' to stop.: "

    guestname = input(message)
    if guestname.lower() != "end":
        append_file(filename, guestname)
    else:
        active = False