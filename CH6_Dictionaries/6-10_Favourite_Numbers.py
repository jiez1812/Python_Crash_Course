fav_nums = {
    'Joe' : [12, 24, 25],
    'Jacq' : [18, 74],
    'Moz' : [5, 42, 2],
    'Xian' : [20, 92],
    'Paw' : [26, 84, 55, 76]
}

for name, numbers in fav_nums.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))
    print()