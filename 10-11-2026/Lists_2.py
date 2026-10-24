# 3 - 4 Guest List
guests = ['Grace', 'Sarah', 'KJ', 'Eric']
message = 'Hey' + ' ' + guests[0] + ', hope you can make it to the party this Sat!'
print(message)
message = 'Hello ' + guests[1] + ', are you able to attend the party?'
print(message)
message = guests[2] + '. ' + 'You are invited to attend the party this weekend!'
print(message)
message = guests[-1] + '. ' + 'Please let us know your availability for this weekend.'
print(message)

print(guests)

# 3 - 5 Changing Guest List
popped_guest = guests.pop(-1)
message = popped_guest + ', ' + 'was unable to attend the party.'
print(message)
guests.append('Molly')
message = '\nHello' + ' ' + guests[-1] + ', ' + 'you are invited to the party.'
print(message)
message = '\nHello' + ' ' + guests[-2] + ', ' + 'you are invited to the party.'
print(message)
message = '\nHello' + ' ' + guests[1] + ', ' +  'you are invited to the party.'
print(message)
message = '\nHello' + ' ' + guests[0] + ', ' + 'you are invited to the party.'
print(message)

# sorting
'''
guests.sort()
print(guests)

guests.sort(reverse=True)
print(guests)
'''
print('\nThis is the list of guests sorted alphabetically')
print(sorted(guests))
print('\nThis is the list of guests sorted in reversed')
print(sorted(guests, reverse=True))
print('\nThis is the original list.')
print(guests)

guests.reverse()
print('\nThis is the guest list after using the reverse method')
print(guests)

print('How many guests will be attending this party?', len(guests))
