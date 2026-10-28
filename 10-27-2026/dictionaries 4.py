# A Dictionary in a Dictionary
'''
reference for my dictionary
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
'''
players = {
    'player_0': {'fname': 'Gabby', 'lname': 'Williams', 'points': 0},
    'player_1': {'fname': 'Kaitlyn', 'lname': 'Chen', 'points': 0},
    'player_2': {'fname': 'Laeticia', 'lname': 'Amihere', 'points': 0},
    'player_3': {'fname': 'Juste', 'lname': 'Jocyte', 'points': 0},
    'player_4': {'fname': 'Kayla', 'lname': 'Thornton', 'points': 0},
    'player_5': {'fname': 'Kaila', 'lname': 'Charles', 'points': 0},
    'player_6': {'fname': 'Miela', 'lname': 'Sowah', 'points': 0},
    'player_7': {'fname': 'Ashten', 'lname': 'Prechtel', 'points': 0},
    'player_8': {'fname': 'LLiana', 'lname': 'Rubert', 'points': 0},
    'player_9': {'fname': 'Janelle', 'lname': 'Salaun', 'points': 0},
    'player_10': {'fname': 'Tiffany', 'lname': 'Hayes', 'points': 0},
    'player_11': {'fname': 'Veronica', 'lname': 'Burton', 'points': 0},
    'player_12': {'fname': 'Cecilia', 'lname': 'Zandalasini', 'points': 0},
    'player_13': {'fname': 'Aminata', 'lname': 'Gueye', 'points': 0},
    'player_14': {'fname': 'Kiah', 'lname': 'Stokes', 'points': 0},
}

for player, player_info in players.items():
    print("\nPlayer: " + player)
    full_name = player_info['fname'] + " " + player_info['lname']
    print("\tFull name: " + full_name.title())