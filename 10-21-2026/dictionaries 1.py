# Dictionaries
valkyries_players = ['Gabby Williams',
                     'Kaitlyn Chen',
                     'Laeticia Amihere',
                     'Juste Jocyte',
                     'Kayla Thornton',
                     'Kaila Charles',
                     'Miela Sowah',
                     'Ashten Prechtel',
                     'LLiana Rupert',
                     'Janelle Salaun',
                     'Tiffany  Hayes',
                     'Veronica Burton',
                     'Cecilia Zandalasini',
                     'Aminata Gueye',
                     'Kiah Stokes']
# collection of key-value pairs
player_0 = {'fname': 'Gabby', 'lname': 'Williams', 'points': 7}
print(player_0['fname'])
print(player_0['lname'])


new_points = player_0['points']
print(player_0['fname'] + ' ' + player_0['lname'] + ' earned ' + str(new_points) + ' points!')

# adding new key-value pairs into dictionary
player_0['jersey_number'] = '1'
player_0['height'] = '5-11'
print(player_0)

# starting with an empty dictionary for Kaitlyn Chen
player_1 = {}
player_1['fname'] = 'Kaitlyn'
player_1['lname'] = 'Chen'
player_1['points'] = 2
player_1['jersey_number'] = '2'
player_1['height'] = '5-9'
print(player_1)

# modifying values in a dictionary