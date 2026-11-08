playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx']

#append
playoff_teams.append('Mystics')
print(playoff_teams[-1])
print(playoff_teams)
#insert
playoff_teams.insert(6, 'Dreams')
print(playoff_teams)

#Removing Elements from a list
# del
del playoff_teams[1] #because wings lost against valks
print(playoff_teams)
del playoff_teams[4] #because Lynx lost against Liberty
print(playoff_teams)

#appending Wings and Lynx so I can use pop method
playoff_teams.append('Wings')
playoff_teams.append('Lynx')
print(playoff_teams)

#Popped - pop() method removes the last item in a list
print("The current teams in the playoffs are", playoff_teams)
eliminated_team = playoff_teams.pop(7)
print("The eliminated team is", eliminated_team)
eliminated_team = playoff_teams.pop(6)
print("The eliminate team are", eliminated_team)

# Removing an Item by Value
print(playoff_teams)
playoff_teams.remove('Fever')
print(playoff_teams)