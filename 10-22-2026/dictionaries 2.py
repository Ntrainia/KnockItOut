# Modifying Values in a Dictionary
player_1 = {}
player_1['fname'] = 'Kaitlyn'
player_1['lname'] = 'Chen'
player_1['points'] = 2
player_1['jersey_number'] = '2'
player_1['height'] = '5-9'
print(player_1)

player_1['jersey_color'] = 'Black'
print("Today, Chen is wearing the " + player_1['jersey_color'] + ' jersey.')
player_1['jersey_color'] = 'White'
print("Today, Chen is wearing the " + player_1['jersey_color'] + ' jersey.')

player_1['x_position'] = 0
player_1['y-position'] = 25
player_1['speed'] = 'medium'
print("Original x-position: " + str(player_1['x_position']))

# Move Chen to the right
# Determine how far to move Chen based on her current speed
if player_1['speed'] == 'slow':
    x_increment = 1
elif player_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

player_1['x_position'] = player_1['x_position'] + x_increment
print("New x-position: " + str(player_1['x_position']))

# Removing Key-Value Pairs
print(player_1)
del player_1['points'] # deletes permanently
print(player_1)

# A Dictionary of Similar Objects
valkyries_players_roles = {
    'Gabby Williams': 'Forward',
    'Kaitlyn Chen': 'Guard',
    'Laeticia Amihere': 'Forward',
    'Juste Jocyte': 'Guard-Forward',
    'Kayla Thornton': 'Forward',
    'Kaila Charles': 'Guard-Forward',
    'Miela Sowah': 'Guard',
    'Ashten Prechtel': 'Forward',
    'Iliana Rupert': 'Center',
    'Janelle Saluan': 'Forward',
    'Tiffany Hayes': 'Guard',
    'Vernonica Burton': 'Guard',
    'Cecilia Zandalasini': 'Foward',
    'Aminata Gueye': 'Center',
    'Kiah Stokes': 'Center'
}

print("Tiffany Hayes's role is " +
      valkyries_players_roles['Tiffany Hayes'])

# Looping Through a Dictionary
for key, value in valkyries_players_roles.items():
    print("\nPlayer: " + key)
    print("Role: " + value)
''' 
key and value can be replaced with anything
for player, role in valkyries_players_roles.items():
    print("\n" + player.title() + "'s role is " + role.title() + ".")
'''

for player in valkyries_players_roles.keys():
    print(player.title())