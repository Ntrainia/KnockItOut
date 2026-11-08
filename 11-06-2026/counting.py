# version 1: will not loop forever
x = 1
while x <= 5:
    print(x)
    x += 1

# version 2: will loop forever
x = 1
while x <= 5:
    print(x)

'''
I made this its own script to see the difference because I was
originally confused, but it makes sense now.

For version 2, x will remain 1 and 1 is always less than 5. Therefore, the while loop
is going to keep printing out 1 infinitely.
'''
