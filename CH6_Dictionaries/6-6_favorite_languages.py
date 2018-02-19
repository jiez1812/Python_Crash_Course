favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

participate_list = ['sarah' , 'harry', 'edward', 'jen', 'mako', 'phil']

for name in participate_list:
    print(name.title())
    if name in favorite_languages.keys():
        print(' Thank you for responding')
    else:
        print(' You are invited to take the poll.')