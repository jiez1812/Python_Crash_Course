def add_reason(filename, reason):
    with open(filename, 'a') as file_object:
        file_object.write(reason + "\n")

filename = 'programming poll.txt'

active = True
while active:
    message = "Please tell us why you like programming? (enter 'end' to stop):"

    respond = input(message)
    if respond.lower() != 'end':
        add_reason(filename, respond)
    else:
        active = False