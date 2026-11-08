import sys #got this from reddit
# Login page
print("Welcome to KnockItOut!")
answer = 'Yes'

input("Are you ready to knock off items on your list or add some? Answer 'Yes' to continue:")
if answer == 'Yes':
    print("Great! Let's continue!")
else:
    print("Aw, that's too bad. Come back next time!")
    sys.exit() #this did not resolve my issue that I mentioned in the description. I will look further into this eventually



# Todo_list
todo_list = []

# adding personal tasks
todo_list.append('Brush teeth')
todo_list.append('Clean room')
todo_list.append('Study')
todo_list.append('Walk the dog')
todo_list.append('Code')
print('These are your tasks:',todo_list)

# remove brush teeth using two methods del & pop
del todo_list[0]
print('These are your tasks: ', todo_list)

popped_task = todo_list.pop(-1)
print('You completed ' + popped_task + "!\n" + "This is your list now", todo_list)

# check the amount of items in your list
amount = len(todo_list)
print('This is how many tasks you have on your to-do list:', amount)

