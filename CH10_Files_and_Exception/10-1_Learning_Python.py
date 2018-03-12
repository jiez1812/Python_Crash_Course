filename = 'learning_python.txt'

def build_header(header, breakline=False):
    if breakline == True:
        print()
    print("-"*5 + header + "-"*5)

build_header("Reading in the entire file")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

build_header("Looping over the file object", True)
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

build_header("Storing the lines in a list", True)
with open(filename) as file_object:
    lines = file_object.readlines()

content = ""
for line in lines:
    content += line

print(content)