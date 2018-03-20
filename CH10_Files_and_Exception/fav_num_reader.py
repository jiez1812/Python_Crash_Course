import json

filename = 'fav_num.json'
with open(filename) as f_obj:
    fav_num = json.load(f_obj)
    print("I know your favorite number! It's {0}.".format(fav_num))