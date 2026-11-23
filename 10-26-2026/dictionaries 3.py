# Nesting - a set of dictionaries in a list or a list of items as a value in a dictionary
'''
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
# A List of Dictionaries
player_0 = {'fname': 'Gabby', 'lname': 'Williams', 'jersey_number': '1', 'position': 'Forward', 'points': 0}
player_1 = {'fname': 'Kaitlyn', 'lname': 'Chen', 'jersey_number': '2', 'position': 'Guard', 'points': 0}
player_2 = {'fname': 'Kaila', 'lname': 'Charles', 'jersey_number': '6', 'position': 'Guard-Forward', 'points': 0}
player_3 = {'fname': 'Tiffany', 'lname': 'Hayes', 'jersey_number': '15', 'position': 'Guard', 'points': 0}
player_4 = {'fname': 'Kiah', 'lname': 'Stokes', 'jersey_number': '41', 'position': 'Center', 'points': 0}

players = [player_0, player_1, player_2, player_3, player_4]
for player in players:
    print(player)

# how do i make a key-value list that would repeat
'''
player = []
for player_number in range(15):
    new_player = {'fname': 'Kiah', 'lname': 'Stokes', 'jersey_number': '41', 'position': 'Center', 'points': 0}
    players.append(new_player)

for player in players[:5]:
    print(player)
print("...")
'''

# A List in a Dictionary
valkyries_roster = {
    'head_coach': 'Natalie Nakase',
    'assistant_coach': ['Sugar Rodgers', 'Kasib Powell', ' Landon Tatum'],
    'trainer': 'Katelin Knox',
    'players': ['Gabby Williams',
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
                     'Kiah Stokes'],
}

print("The Valkyries are led by head coach " + valkyries_roster['head_coach'] + "."
      + "\nThe Valkyries consist of players:")
for player in valkyries_roster['players']:
    print("\t" + player)

valkyries_players = {'Gabby Williams' : 'Forward',
                     'Kaitlyn Chen': 'Guard',
                     'Laeticia Amihere': 'Foward',
                     'Juste Jocyte': 'Guard-Forward',
                     'Kayla Thornton': 'Forward',
                     'Kaila Charles': 'Guard-Forward',
                     'Miela Sowah': 'Guard', # Developmental Player
                     'Ashten Prechtel': 'Forward', # Developmental Player
                     'LLiana Rupert': 'Center',
                     'Janelle Salaun': 'Forward',
                     'Tiffany  Hayes': 'Guard',
                     'Veronica Burton': 'Guard',
                     'Cecilia Zandalasini': 'Forward',
                     'Aminata Gueye': 'Center',
                     'Kiah Stokes': 'Center',
                     }
for player, position in valkyries_players.items():
    print("\n" + player.title() + "'s position is: " + position)