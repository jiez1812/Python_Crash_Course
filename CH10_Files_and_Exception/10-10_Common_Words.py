filename = 'A Manual of Ancient History.txt'

with open(filename, encoding="utf-8") as file_obj:
    contents = file_obj.read()
    the_count = contents.lower().count('the')
    print(the_count)