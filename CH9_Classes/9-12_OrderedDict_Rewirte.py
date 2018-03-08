from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['victoria'] = 'c'
favorite_languages['jacq'] = 'go'
favorite_languages['nyx'] = 'python'

for name, language in favorite_languages.items():
    print("{0}'s favorite language is {1}.".format(name.title(), language.title()))