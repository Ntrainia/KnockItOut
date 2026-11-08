# the past two days (10-17-2026 & 10-18-2026) played around with if statements
#if-else Statements
playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx', 'Dream', 'Mystics']
eastern_conference = ['Dream', 'Sky', 'Sun', 'Fever', 'Liberty', 'Tempo', 'Mystic']
# ^^^ this is a tuple since these teams are always going to exist in the WNBA eastern conference
western_conference = ['Wings', 'Valkyries', 'Aces', 'Sparks', 'Lynx', 'Mercury', 'Fire', 'Storm']

team = input('Put in your WNBA team to find out if they are in the playoffs:')
if team in playoff_teams:
    print('Yes the ' + team + ' are in the Playoffs!')
else:
    print("Eek, unfortunately! Nope!")

#if-else Statements & Multiple elif Blocks
team = len(playoff_teams)

print('What phase is the WNBA season in?')
if team >= 7: #understand the math in Python cause these change of sign makes the difference
    print('The playoffs are have began!\nThese are the teams competing:')
    for team in playoff_teams:
        print(team)
elif team >= 4:
    print('The WNBA are in the semifinals!\nThese are the teams competing')
    for team in playoff_teams:
        print(team)
elif team <= 2:
    print('The WNBA are in the finals!\nThese are the teams competing')
    for team in playoff_teams:
        print(team)
else: #else block can be omitted (this is helpful since I didn't realize this in my python scripts)
    print('The WNBA season has ended')

# testing multiple conditions
if 'Valkyries' in playoff_teams:
    print("The Valkyries are in the playoffs")
if 'Wings' in playoff_teams:
    print("The Wings are in the playoffs")
if 'Aces' in playoff_teams:
    print("The Aces are in the playoffs")

print('\nThe following teams are in the playoffs')

# If-statements can be repeated consecutively, but if elif else statements depend on the condition of previous statements
