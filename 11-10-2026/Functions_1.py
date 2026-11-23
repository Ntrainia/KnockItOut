'''
Functions: named blocks of code that are designed to one specific job
Modules: allow us to store functions in separate files
'''

def greet_user(username): # function definition that tells Python name of function and information needed for function to do its job
    '''Display a simple greeting. <- This is a docstring'''
    print("Hello, " + username.title() + "!")

greet_user('Mordecai') #username is a parameter, a piece of information the function needs to do its job
greet_user('Rigby') # 'Mordecai' and 'Rigby' is an example of an argument, a piece of information that is passed from a function call to a function

# Arguments and Parameters