def show_magicians(names):
    print("The Magician List is shown as below: ")
    for name in names:
        print("\t- {0}".format(name.title()))

names = ['harry', 'ron', 'hermione']
show_magicians(names)