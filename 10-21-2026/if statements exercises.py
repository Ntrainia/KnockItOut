# 5-8. Hello Admin:

usernames = ['admin',
             'valksfan101',
             'chensanity',
             'bballmonster',
             '01superFT']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + username + ', thank you for logging in again.')

# 5-9. No Users:
usernames = []
if usernames == []:
    print('We need  to find some users!')

# 5-10. Checking Usernames:
current_usernames = ['admin',
             'valksfan101',
             'chensanity',
             'bballmonster',
             '01superFT']
new_usernames = ['kaia12',
                 'chensanity',
                 'HayesSuperFan',
                 'bballmonster',
                 'WNBAfanatic']


for new_user in new_usernames:
    if new_user in current_usernames:
        print('Error! This username has been taken. Create a new one.')
    else:
        print('Good to go! Enjoy your username, ' + new_user)

# 5-11. Ordinal Numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number >= 4:
        print(str(number) + 'th')
    elif number == 3:
        print(str(number) + 'rd')
    elif number == 2:
        print(str(number) + 'nd')
    else:
        print(str(number) + 'st')
