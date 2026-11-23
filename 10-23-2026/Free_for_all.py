# Goal - create a dictonary for a Valks player and a script that calculates shot percentages

player_0 = {'fname': 'Kaila',
            'lname': 'Charles',
            'team': 'Valkyries',
            'jnumber': '6',
            'role': 'Forward and Guard',
            'height': "6'1",
            'status': True,
            'point': 0}

# make a point system where points are added up
'''
Player score 3 points for any basket made beyond the 3 point line, in bounds
Player score 2 points for any basket made inside the 3 point line, in bounds
Player score 1 point for made free throws
'''
# field_goal = 0

'''
planning:
if player_0 shoots beyond the 3 point line:
    print('+3 points!')
elif player_0 shoots inside the 3 point line:
    print('+2 points!')
elif player_0 shoots at ft_line:
    print('+1 point!s')
else:
    print('Missed!')
    
I need to make variables, but I am having trouble
    
'''

# points = ['b3pt', 'in3pt', 'ft_line'] - options
og_pt = player_0['point']
threept = 3
twopt = 2
ftpt = 1

'''
guidance from python crash course
player_1['x_position'] = player_1['x_position'] + x_increment
print("New x-position: " + str(player_1['x_position']))
'''

points = 'b3pt'
if points == 'b3pt':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(threept) + "!")
    player_0['point'] = player_0['point'] + threept
elif points == 'in3pt':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(twopt) + "!")
    player_0['point'] = player_0['point'] + twopt
elif points == 'ft_line':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(ftpt) + "!")
    player_0['point'] = player_0['point'] + ftpt
else:
    print('Missed basket!')

print('\n' + player_0['fname'] + " " + player_0['lname'] +
      " has a total of " + str(player_0['point']) + " points!")

points = 'in3pt'
if points == 'b3pt':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(threept) + "!")
    player_0['point'] = player_0['point'] + threept
elif points == 'in3pt':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(twopt) + "!")
    player_0['point'] = player_0['point'] + twopt
elif points == 'ft_line':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(ftpt) + "!")
    player_0['point'] = player_0['point'] + ftpt
else:
    print('Missed basket!')

print('\n' + player_0['fname'] + " " + player_0['lname'] +
      " has a total of " + str(player_0['point']) + " points!")

points = 'ft_line'
if points == 'b3pt':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(threept) + "!")
    player_0['point'] = player_0['point'] + threept
elif points == 'in3pt':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(twopt) + "!")
    player_0['point'] = player_0['point'] + twopt
elif points == 'ft_line':
    print(player_0['fname'] + " " + player_0['lname'] +
          " " + "scored " + str(ftpt) + "!")
    player_0['point'] = player_0['point'] + ftpt
else:
    print('Missed basket!')

print('\n' + player_0['fname'] + " " + player_0['lname'] +
      " has a total of " + str(player_0['point']) + " points!")