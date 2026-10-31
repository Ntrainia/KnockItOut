number = input("Enter a number to determine whether its odd or even: ")
number = int(number)

if number % 2 == 0: # if number divided by 2 has a remainder of 0
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
