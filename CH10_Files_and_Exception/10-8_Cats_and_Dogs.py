def read_file(filename):
    try:
        with open(filename) as file_obj:
            content = file_obj.read()
    except FileNotFoundError:
        print("The file " + filename + " is not found.")
    else:
        print(content)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_file(filename)