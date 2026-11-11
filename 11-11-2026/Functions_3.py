# Keyword arguments: name-value pair that you pass to a function
def describe_character(character_species, character_name):
    """Display information about a character in Regular Show."""
    print("\nMy favorite character in Regular Show is " + character_name)
    print(character_name + "'s species in Regular Show is a " + character_species)

# order doesn't matter because parameter is match with argument
describe_character(character_species = 'raccoon', character_name = 'Rigby')
describe_character(character_name = 'Mordecai', character_species = 'blue jay')

# Default Values
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name = 'Lucky')