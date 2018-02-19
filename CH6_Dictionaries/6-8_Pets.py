mob = {'kind': 'puppy', 'owner': 'john'}
niel = {'kind': 'kitty', 'owner': 'amier'}
boon = {'kind': 'pig', 'owner': 'kate'}

pets = [mob, niel, boon]

for pet in pets:
    print("Kind : " + pet['kind'].title())
    print("Owner : " + pet['owner'].title() + "\n")