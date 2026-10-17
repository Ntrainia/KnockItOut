# 4-2 Animals (exercise to start off today's session)

animals = ['Cheetah', 'Zebra', 'Pig', 'Dog', 'Cat', 'Shark']
animals.sort()
print(animals)

for animal in animals:
    print("A" + " " + animal + " " + "would absolutely shred you to pieces.")
    print("But they're absolutely adorable!\n")
print("Thank you for visiting our animals.")

# Numerical Lists (I need this for my To-Do list)
# range() method!
'''
for value in range(1,5):
    print(value)
'''
# range() to make a list of numbers (I added a for loop for fun)
'''
numbers = list(range(1,6)) #this is considered wrapping list() around a call to the range() function
for number in numbers:
    print(number)
'''

# skip count
even_numbers = list(range(2,11,2)) # (2, 11, 2) first 2 - starts with number 2, 11 - ends at 11 (since index 0 = off-count), last 2 - adds 2
print(even_numbers)

# any set of numbers using range()
squares = []
for value in range(1,11):
    print(squares) #lets me see the loop happening to each value
    square = value**2
    squares.append(square)
print(squares)

# simple statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (min(digits))
print (max(digits))
print (sum(digits))

# list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
