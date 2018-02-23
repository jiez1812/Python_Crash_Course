# Multiple Function Calls

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a {0}.".format(animal_type))
    print("My {0}'s name is {1}.".format(animal_type, pet_name.title()))

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')