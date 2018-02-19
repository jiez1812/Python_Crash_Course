favorite_places = {
    'eric' : ['Shadeport', 'Maplehollow', 'Rosewater'],
    'faye' : ['Esterglass', 'Misthall', 'Estershade'],
    'georges' : ['Vertway', 'Marbleash'],
    'randy' : ['Woodcrest', 'Glassnesse'],
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places:")
    for place in places:
        print("\t- " + place)
    print("")