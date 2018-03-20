import json

fav_num = int(input("What's your favorite number?"))
filename = 'fav_num.json'
with open(filename, 'w') as f_obj:
    json.dump(fav_num, f_obj)
    print("I've saved your favorite number (" + str(fav_num) + ")!")