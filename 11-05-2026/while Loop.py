# the while Loop in Action
current_number = 0
while current_number <= 10:
    print(current_number)
    current_number += 2

# ^^^ adjusted the while Loop in action to skip count by 2

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
prompt += "\nEnter here: "
# ^ I don't particularly like the way this is formated in the text so I adjusted it.

message = "" # empty string for python to compare something to
while message != 'quit':
    message = input(prompt)
    print(message)

    if message != 'quit':
        print(message)

# Using a Flag (-a signal to the program)