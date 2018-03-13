filename = 'progamming.txt'

""" read mode('r') / write mode ('w') / append mode ('a') """

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")