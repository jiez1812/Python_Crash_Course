glossary = {
    'Chap_1': 'Introduction',
    'Chap_2': 'Basics',
    'Chap_3': 'Intro Lists',
    'Chap_4': 'Works with Lists',
    'Chap_5': 'If Statements',
    'Chap_6': 'Dictionaries',
    'Chap_7': 'User Input And While Loops',
    'Chap_8': 'Functions',
    'Chap_9': 'Classes',
    'Chap_10': 'Files and Exceptions'
    }

print('\tChapter\t|\tTitle')
print('-'*40)
for k, v in glossary.items():
    print("\t" + k + "\t|\t" + v)