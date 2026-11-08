# ^^^ anything within quotation marks is a string. What is a string? A series of characters
'''
name = "ngoc tran"
print(name.title())

name = "NGOC TRAN"
print(name.title()) regardless of how I do it, it'll come out as Ngoc Tran
title() is a method
A method is an action that Python can perform on piece of data
The dot after name tells the method title() to act on variable name
'''

lowercaseName = 'NGOC TRAN'
print(lowercaseName.lower())
uppercaseName = 'ngoc tran'
print(uppercaseName.upper())
name = 'ngOc TraN'
print(name.title())

# Combining or Concatentating Strings
first_name = 'Ngoc'
middle_name = 'Hoang'
last_name = 'Tran'
full_name = first_name + " " + middle_name + " " + last_name
print(full_name)
print(full_name.upper())
print(full_name.lower())

print ("Hello", full_name.title(), "!") #when I add this comma, there's a space for whatever reason
print ("Hello", full_name.title() + "!")

print("Python")
print("\tPython") #\t adds whitespace

print("Tran Siblings:\nNgoc\nKhang\nMinh\nNhung") #\n new line
print("Tran Siblings:\n\tNgoc\n\tKhang\n\tMinh\n\tNhung") #can use both








