message= "Hello world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
# variable names can only contain letters, numbers, and underscores
# cannot start with number
# no spaces
message = "I'm going to create an error on purpose"
print(mesage)

'''
Traceback (most recent call last):
  File "C:\Users\ntran\KnockItOut\Tutorials\hello_world.py", line 10, in <module>
    print(mesage) (what kind of error it found)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'? (Type of error) 
'''