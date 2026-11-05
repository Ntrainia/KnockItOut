# 7-4. Pizza Toppings:
prompt = input("\nEnter your choice of pizza toppings: ")
prompt += input("Enter 'quit' when you are finished. ")

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(toppings + " has been added onto your pizza!")

# 7-5. Movie Tickets:
'''
person under age of 3, ticket is free
person < 2
person age between 3 and 12
person < 13
'''
prompt = input("\nEnter your age for movie price: ")
person = int(input(prompt))

if person < 2:
    print("Your ticket is free.")
elif person < 13:
    print("Your ticket is $10")
elif person > 13:
    print("Your ticket is $15")

# i am in a slump. I'll be back.