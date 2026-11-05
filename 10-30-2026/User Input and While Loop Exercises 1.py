# 7-1. Rental Car:
rental_car = input("Enter the kind of rental car you would like: ")
print("Let me see if I can find you a " + rental_car + ".")

# 7-2. Restaurant Seating:
number_of_people = input("Enter the number of people in dinner group: ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3. Multiple of Ten:
number = input("Enter a number to see if the number is a multiple of 10 or not: ")
number = int(number) #forgot to add this initially

if number % 10 == 0:
    print(str(number) + " is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10.")