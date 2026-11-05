# Today's practice I want to focus on the math a bit more
# I realize I should finish the chapter before focusing on my weaknesses

#Checking Whether a Value Is in a List
playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx']
# going back to make an if statement
team = input('Type in your WNBA team name to see if they are in the playoffs:')
if team in playoff_teams:
    print('Yes. The team, ' + team.title() + ', is in the playoffs.')
else:
    print('Error.')


print('Valkyries' in playoff_teams)
print('Fire' in playoff_teams)

#Checking Whether a Value Is Not in a List
dropped_teams = ['Fire', 'Sparks', 'Mercury', 'Tempo', 'Sun', 'Storm']
team = 'Valkyries'

if team not in dropped_teams:
    print(team.title() + ' will be playing in the playoffs.')

# Boolean Expressions - another name for a conditional test
'''
examples
game_active = True
can_edit = False
'''

# simple if statements
lose_streak = 5

if lose_streak >= 5:
    print('Time to get off Val!')