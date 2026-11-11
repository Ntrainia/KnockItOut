# Passing Arguments
'''
Function definitions can have multiple parameters
position arguments; need to be in the same order the parameters were written
'''

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'Harry')
describe_pet('dog', 'Lucky')
describe_pet('Sally', 'panda') # purposeful error
