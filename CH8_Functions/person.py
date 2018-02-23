# Returning a Dictionary

def build_persion(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_persion('jimi', 'hendrix', age=27)
print(musician)