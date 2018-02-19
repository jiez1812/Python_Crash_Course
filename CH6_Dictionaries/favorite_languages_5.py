# Looping through a Dictionary's Keys in Order

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

friends = ['phil', 'sarah']

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")