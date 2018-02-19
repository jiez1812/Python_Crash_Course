cities = {
    'Kuala Lumpur' : {
        'country' : 'Malaysia',
        'population' : 1.589,
        'fact' : 'Capital of Malaysia',
    },
    'Ulaanbaatar': {
        'country' : 'Mongolia',
        'population' : 1.38,
        'fact' : 'Capital of Mongolia',
    },
    'Reykjavik': {
        'country' : 'Iceland',
        'population' : 0.122,
        'fact' : 'Capital of Iceland',
    },
}

for city, city_info in cities.items():
    print(city + ": -")
    for k, v in city_info.items():
        if k == 'population':
            k = 'population (million)'
        print("\t" + k.title() + " : " + str(v).title())
    print()