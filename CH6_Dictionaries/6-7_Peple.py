person_1 = {'first_name' : 'Joe', 'last_name' : 'Kim', 'age' : 24, 'city' : 'Seoul'}
person_2 = {'first_name' : 'Harry', 'last_name' : 'Windsor', 'age' : 24, 'city' : 'London'}
person_3 = {'first_name' : 'Noctics', 'last_name' : 'Lucis', 'age' : 24, 'city' : 'Insomnia'}

people = [person_1, person_2, person_3]

for person in people:
    print("First Name : " + person['first_name'])
    print("Last Name : " + person['last_name'])
    print("Age : " + str(person['age']))
    print("City: " + person['city'] + "\n")