playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx', 'Dream', 'Mystics']

# demonstration of a loop
for team in playoff_teams: #Python pulls a name from list playoff_teams and store it in the variable team
    print(team)

for team in playoff_teams:
    print(team.title() + ", welcome to the WNBA playoffs!")
    print("Make sure to get proper rest, " + team.title() + "!\n")
print('Congratulations on getting here!')
