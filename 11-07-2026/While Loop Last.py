# Moving Items from One List to Another
# Start with users that need to be verified
# and an empty list to hold confirmed users
# will adjust variables to match my situation

invited_guests = ['Mordecai', 'Margaret', 'Rigby', 'Eileen', 'Benson', 'Skips', 'Pops']
confirmed_guests = []

# Verify each guest until there are no more unconfirmed guests
# Move each verified guest into the list of confirmed users


active = True
while invited_guests:
    name = input("\nEnter your name: ")
    name += input("\nEnter 'quit' if you wish to exit.")
    if name != 'quit':
        if name in invited_guests:
            print(name)
            confirmed_guests.append(name)
            print("Confirming invitee: " + name.title())
            name = invited_guests.remove(name)# this pops a random member in list
        else:
            break
    elif name == 'quit':
        active = False
        break

print("\nThe following users have been confirmed: ")
for confirmed_guests in confirmed_guests:
    print(confirmed_guests.title())