# Exercise 1: Basic Dictionary Operations

student = {"name": "Alice", "age": 20, "grade": "B"}

#Expected Output: {"name": "Alice", "age": 21, "grade": "B", "city": "New York"} and Name: Alice
student["age"] = 21
student["grade"] = "B"
student["city"] = "New York"
print(student)

print("Name: " + student["name"])

# Exercise 2: Dictionary Operations
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"} #given input

'''
{'brand': 'Toyota', 'model': 'Camry', 'year': 2022}
dict_items([('brand', 'Toyota'), ('model', 'Camry'), ('year', 2022)])
'brand' exists: True
'color' exists: False
'''
car.pop("color")
print(car)
print(car.items())
print("'brand' exists:", 'brand' in car)# corrections done since I forgot the "'brand' exists:"
print("'color' exists:", 'color' in car) # corrections done since I forgot the "'color' exists:"

# Exercise 3: Dictionary from Two Lists
keys = ["name", "age", "city"] # given input
values = ["Bob", 25, "London"] #given input

# Expected Output: {'name': 'Bob', 'age': 25, 'city': 'London'}
'''
I am expected to map, but I didn't remember coming across it.
Using hints, it suggested I use zip(keys, values)
'''
print(dict(zip(keys, values))) # that was easier than I thought

# Exercise 4: Clear Dictionary
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
# Expected Output: {}
inventory.clear()
print(inventory)

# Exercise 5: Merge Dictionaries
'''
This is another concept I didn't come across in the textbook, but it feels like
it'll come in handy.

Using hints, it suggests I can try two different ways.
update or merged
'''
dict1 = {"a": 1, "b":2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2
print(merged)
