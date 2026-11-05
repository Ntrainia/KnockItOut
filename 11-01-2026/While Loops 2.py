# while Loop in Action
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit
prompt = "\n..."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# ^ I did try another variant of this in a privious

# Using a Flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# ^^^ use this

# break to exit a loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# I got lazy and am feeling impatient so I will do the exercises
