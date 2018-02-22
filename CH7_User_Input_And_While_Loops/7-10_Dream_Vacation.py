result = {}
polling_active = True

while polling_active:
    name = input("What's your name?")
    response = input("If you could visit one place in the world, where would you go? ")

    result[name] = response

    repeat = input("Next participant? (Y/N): ")
    if repeat.upper() == 'N':
        polling_active = False

print("\n{0}Result{0}".format("#"*5))
print("\tName\t|\tPlace\t")
print("-"*40)
for name, place in result.items():
    print("\t{0}\t|\t{1}\t".format(name, place))