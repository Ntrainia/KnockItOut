#Anh Duy suggested that ask user for total games played, games won, games lost


# Have a list of banned_players
while True:
    banned_players = ['Diana', 'Ethan','Elsa', 'Kien', 'Andy', 'Kore']
    user = (input('Input your first name here:'))
    if user in banned_players:
        print('You are banned from Valorant.')
    else:
        print('Have fun playing Valorant!')
        break
print('MUHWHAHAHA')


while True:
    total = int(input('How many games have you played so far?\n Answer:'))
    lose_streak = int(input('How many games have you lost?\n Answer:'))

    percentage = lose_streak/total

    if percentage <= 0.55:
        print('You may play more.')
    else:
        print('System shut down. No more Val for you.\nPractice on AimLabs.')
        break
