rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon river': 'brazil'
}

for river, country in rivers.items():
    print('The {0} runs through {1}'.format(river.title(), country.title()))

print('\nThe following rivers are mentioned: ')
for river in rivers.keys():
    print('\t- ' + river.title())

print('\nThe following countries are mentioned: ')
for country in rivers.values():
    print('\t- ' + country.title())