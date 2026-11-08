'''
for loop - takes a collection of items and executes a block of code once for each item in the collection
while loop - runs as long or while, a certain condition is true
'''

# The while loop in action
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
number_of_players = len(valkyries_players)
while number_of_players <= 15:
    print(number_of_players)
    number_of_players += 1 #do not -= 1, it goes crazy