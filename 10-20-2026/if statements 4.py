# if statements with lists
playoff_teams = ['Valkyries', 'Wings', 'Aces', 'Fever', 'Liberty', 'Lynx', 'Dream', 'Mystics']

# Checking for Special Items
for team in playoff_teams:
    if team == 'Valkyries':
        print("The Valkyries is Ngoc's favorite team!")
    else:
        print('The ' + team + ' are in the playoffs!')

# Checking That a List is Not Empty
''' How do I make this list more readable instead of this long line
valkyries_players = ['Gabby Williams', 'Kaitlyn Chen', 'Laeticia Amihere', 'Juste Jocyte', 'Kayla Thornton', 'Kaila Charles', 'Miela Sowah', 'Ashten Prechtel', 'LLiana Rupert', 'Janelle Salaun', 'Tiffany  Hayes', 'Veronica Burton', 'Cecilia Zandalasini', 'Aminata Gueye', 'Kiah Stokes']
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

valkyries_coaching_staff = ['Natalie Nakase',
                            'Sugar Rodgers',
                            'Kasib Powell',
                            'Landon Tatum',
                            'Katelin Knox']

# Using Multiple Lists
for player in valkyries_players:
    if player == 'Gabby Williams':
        print('Gabby Williams was recruited by ' + valkyries_coaching_staff[0] + '!')
    else:
        print('Well, this was not the best way to use this example, but here!', player)

print('These are the players in the Valkyries!')

print('\n Congratulations on finishing If Statement Chapter!')