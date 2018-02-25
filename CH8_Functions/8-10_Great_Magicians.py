def show_magicians(names):
    print("The Magician List is shown as below: ")
    for name in names:
        print("\t- {0}".format(name.title()))

def make_great(names, great_names):
    while names:
        current_name = "Great " + names.pop()
        great_names.append(current_name)

names = ['harry', 'ron', 'hermione']
great_names = []

make_great(names, great_names)
show_magicians(great_names)