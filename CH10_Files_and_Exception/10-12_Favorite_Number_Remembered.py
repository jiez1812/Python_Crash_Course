import json

filename = 'fav_num.json'
try:
    with open(filename) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)
        print("I've saved your favorite number (" + str(fav_num) + ")!")
else:
    print("I know your favorite number! It's {0}.".format(fav_num))