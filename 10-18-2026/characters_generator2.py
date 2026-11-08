import random

'''
invitees = ['Kimmy','Grace', 'Ella', 'Eric', 'Sarah', 'Tylor', 'KJ', 'Dana']
invitees.sort()
print(invitees)
characters = ['Main Character', 'Costume Designer', 'Reporter', 'Antagonist', 'Camera Operator', 'Writer', 'Gaffer', 'Co-Star']
characters.sort()
print(characters)
'''
invitees = []
characters = []

while True:
    yes = 'Y'
    no = 'N'
    answer = input("Add your guests with this!\nDo you want to add a guest?\nAnswer 'Y' to continue or 'N' to stop:")
    if answer == yes:
        print('Great!')
        break
    else:
        print('Goodbye.')
        break

while True:
    adding_invitees = (input("If you wish to stop adding, then enter 'stop'. Add your guest here:"))
    if adding_invitees == "stop":
        print('Thank you. Here is your list of invitees')
        for invitee in invitees:
            print(invitee)
        break
    if adding_invitees:
        invitees.append(adding_invitees)

while True:
    adding_characters = (input("If you wish to stop adding, then enter 'stop'. Add your character here:"))
    if adding_characters == "stop":
        print('Thank you. Here is your list of invitees')
        for character in characters:
            print(character)
        break
    if adding_characters:
        characters.append(adding_characters)

print(invitees)
print(characters)

while True:
    yes = 'Y'
    no = 'N'
    answer = input("Do you want to assign your guests with character roles?\nAnswer 'Y' to assign or 'N' to stop:")
    if answer == yes:
        for invitee in invitees:
            random_character = random.choice(characters)
            print(invitee + ' ' + 'is' + ' ' + random_character)
            taken_character = random_character
            assigned_invitee = invitee
            characters.remove(taken_character)
            invitees.remove(assigned_invitee)
            print(taken_character + ' ' + 'is now taken by ' + assigned_invitee)
            break
    if answer == no:
        print('Understood. Goodbye.')
        break


'''
selected = random.choice(invitees.pop()) + random.choice(characters.pop())
random_character = random.choice(characters)
'''

'''
for invitee in invitees:
    random_character = random.choice(characters)
    print(invitee + ' ' + 'is' + ' ' + random_character)
    taken_character = random_character
    characters.remove(random_character)
    print(taken_character + ' ' + 'is now taken.')
'''


'''
selected_invitee = invitees.pop(-1)
selected_character = characters.pop(1) #tried using pop initially, but that did not work because pop() only takes index
print(selected_invitee + ' is ' + selected_characters

'''

