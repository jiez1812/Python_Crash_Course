pets = []

pet = {
    'name' : 'dank',
    'kind' : 'cat',
    'owner' : 'rory'
}
pets.append(pet)

pet = {
    'name' : 'maia',
    'kind' : 'dog',
    'owner' : 'triexie'
}
pets.append(pet)

pet = {
    'name' : 'atlas',
    'kind' : 'pig',
    'owner' : 'donelle'
}
pets.append(pet)

for p in pets:
    print("Name : " + p['name'].title())
    print("Kind : " + p['kind'].title())
    print("Owner : " + p['owner'].title() + "\n")