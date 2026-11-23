# 9-1 and 9-2
class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print two pieces of information"""
        print("The restaurant name is " + self.restaurant_name)
        print("The restaurant's cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

restaurant_1 = Restaurant("McDonald's", "Fast Food")
restaurant_2 = Restaurant("Pho Saigon", "Vietnamese")
restaurant_3 = Restaurant("Sushi Whoo!", "Japanese")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

class User():
    """A simple attempt to model a User."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("User's full name: " + self.first_name + " " + self.last_name)

    def greet_user(self):
        print("Hello! Welcome " + self.first_name + " " + self.last_name)


user_1 = User("Jason", "Derulo")
user_2 = User("Brittany", "Spears")
user_3 = User("Kaitlyn", "Chen")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
