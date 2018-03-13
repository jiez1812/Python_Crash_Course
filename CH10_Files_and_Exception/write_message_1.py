filename = 'progamming.txt'

""" read mode('r') / write mode ('w') / append mode ('a') """

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new game.\n")