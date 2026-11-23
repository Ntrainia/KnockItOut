class Player(): # Capitalized names refer to classes in Python
    """A simple attempt to model a player."""

    def __init__(self, fname, lname, age): # special method that Python runs automatically whenever we create a new instance
        """Initialize name and age attributes."""
        self.fname = fname
        self.lname = lname
        self.age = age

    def offense(self):
        """Simulate a player perform an offensive move."""
        print(self.lname.title() + " has shot the ball!")

    def defense(self):
        """Simulate a player perform a defensive move."""
        print(self.lname.title() + " is protecting the ball")


player_1 = Player('Kaitlyn', 'Chen', 24)
player_2 = Player('Gabby', 'Williams', 30)

print("My favorite player's name is " + player_1.fname.title() + " " + player_1.lname.title() + ".")
print(player_1.fname.title() + " " + player_1.lname.title() + " is " + str(player_1.age) + " years old.")

player_1.offense()
player_1.defense()

player_2.offense()