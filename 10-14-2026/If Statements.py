# Example - adjusted with WNBA in mind
playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx', 'Dream', 'Mystics']

for team in playoff_teams:
    if team == 'Valkyries': #Is the value of team equal to 'Valkyries'?
        print("The" + " " + team.title() + " " + "is Ngoc's top pick in the playoffs!")
    else:
        print("Ngoc is not rooting for this team.")

# Conditional Tests
'''
= sets the value of variable
== checks the value
returns True if match matches
returns False if match does not matches
'''

# Checking for Inequality

for team in playoff_teams:
    if team != 'Valkyries': #will return true if team does not match 'Valkyries'
        print('Error! This is the ' + team)
    else: #false, return
        print('BALLHALAAAA')

# Numerical Comparison
input("What seed is the Valkyries in the play-offs?\nInput a number:")
answer = 2
if answer == 2:
    print("Congratulations! You got it right.")
else:
    print("That is not the correct answer. Please try again.")

# Using and to Check Multiple Conditions
'''
age_0 = 23
age_1 = 16
age_0 >= 21 and age_1 >= 21 
'''

