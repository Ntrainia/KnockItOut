# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
prompt += "\nEnter your prompt here: "

active = True # sets the default script to active so it runs
while active:
    message = input(prompt)

    if message == 'quit': # when the user enters 'quit', that changes the variable to False
        active = False
    else:
        print(message)

# Using break to Exit a Loop
prompt = "\nPlease enter the name of the WNBA team you like."
prompt += "\n(Enter 'quit' when you are finished')"
prompt += "\nTeam: "

while True:
    team = input(prompt)

    if team == 'quit':
        break
    else:
        print("The " + team + " is a great choice!")

# Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # it kind of ignores it, which is why it skip counts
    print(current_number)
