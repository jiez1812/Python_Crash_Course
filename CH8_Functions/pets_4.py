# Default Values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a {0}.".format(animal_type))
    print("My {0}'s name is {1}.".format(animal_type, pet_name.title()))

describe_pet(pet_name='willie')