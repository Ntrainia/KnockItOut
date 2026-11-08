# Lists allow you to store sets of information in one place

tran_siblings = ['Ngoc', 'Khang', 'Minh', 'Nhung']
print(tran_siblings)

#ordered_collection, index
# Ngoc = index 0, Khang = index 1, Minh = index 2, Nhung = index 3
print(tran_siblings[0])
print(tran_siblings[2])
print(tran_siblings[1])
print(tran_siblings[3])

print((tran_siblings[0] + " " + "Tran").title())

print(tran_siblings[-1]) #index -1 always return the last item in the list, -2 returns the second from end of list

message = "Mom and Dad's favorite kid is" + ' ' + tran_siblings[0].title() + '!'
print(message)

message = "Mom and Dad's least favorite kid is" + ' ' + tran_siblings[3].title() + '!'
print(message)

# Exercise 3-1 Names
cousins = ['Julia', 'Diana', 'Kien', 'Khang']
print(cousins[0])
print(cousins[1])
print(cousins[2])
print(cousins[3])

# Exercise 3-2 Greetings
message = 'Hi' + ' ' + cousins[0]
print(message)
