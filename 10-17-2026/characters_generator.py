import random
invitees = ['Kimmy','Grace', 'Ella', 'Eric', 'Sarah', 'Tylor', 'KJ', 'Dana']
invitees.sort()
print(invitees)
characters = ['Main Character', 'Costume Designer', 'Reporter', 'Anatgonist', 'Camera Operator', 'Writer', 'Gaffer', 'Co-Star']
characters.sort()
print(characters)
'''
selected = random.choice(invitees.pop()) + random.choice(characters.pop())
random_character = random.choice(characters)
'''

for invitee in invitees:
    random_character = random.choice(characters)
    print(invitee + ' ' + 'is' + ' ' + random_character)
    taken_character = random_character
    characters.remove(random_character)
    print(taken_character + ' ' + 'has been taken.')

'''
selected_invitee = invitees.pop(-1)
selected_character = characters.pop(1) #tried using pop initially, but that did not work because pop() only takes index
print(selected_invitee + ' is ' + selected_characters

'''
