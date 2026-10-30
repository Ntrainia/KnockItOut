'''
# exercises to start off
# 4-6 Odd Numbers
for value in list(range(1, 21, 2)): # start with value 1, end at value 20, add 2
    print(value)

# 4-7 Threes
for value in list(range(3, 31, 3)):
    print(value)

# 4-8 Cubes
for value in list(range(1,11)):
    cube = value**3
    print(cube)

# Cube Comprehension
cube = [value**3 for value in range(1, 11)]
print(cube)

'''

# Slicing a List
playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx', 'Dream', 'Mystics']
print(playoff_teams[0:3]) #generates at the first index[0] and returns three values

print(playoff_teams[1:4]) #prints second, third, and fourth team

print(playoff_teams[:5]) #omitting first index in slice, automatically starts at beginning of list

print(playoff_teams[5:]) #will start at index 5 and list the remaining teams

print(playoff_teams[-3:]) #print the names of the last three players

# Looping through a slice
print("These are the first four teams competing in the WNBA playoffs:")
for team in playoff_teams[0:4]:
    print('\t'+team.upper())

# Copying a List - neat to know about
'''
playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx', 'Dream', 'Mystics']
myplayoff_teams = playoff_teams[:] #this includes the entire og playoff_teams list

print("The playoff teams for the WNBA is:")
print(playoff_teams)

print("My top personal playoff teams for the WNBA is:")
print(myplayoff_teams)

del myplayoff_teams[2]
'''

# Tuples - immutable lists (values that cannot change)
eastern_conference = ('Dream', 'Sky', 'Sun', 'Fever', 'Liberty', 'Tempo', 'Mystic')
# ^^^ this is a tuple since these teams are always going to exist in the WNBA eastern conference
western_conference = ('Wings', 'Valkyries', 'Aces', 'Sparks', 'Lynx', 'Mercury', 'Fire', 'Storm')
# on a second note, this might be a bad example since there will be expansion teams, but this will work for now

print("These are the teams in the WNBA Eastern Conference:")
for team in eastern_conference:
    print("\t"+team.upper())

print("These are the teams in the WNBA Western Conference:")
for team in western_conference:
    print("\t"+team.upper())

# tuples can't be modified, but they can be assigned new values to the variable that holds that tuple

congratulations = "\nYou finish Chapter 4! WHOOO"
print(congratulations)