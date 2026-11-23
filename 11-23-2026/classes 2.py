class Player():
    """A simple attempt to represent a player."""
    def __init__(self, fname, lname, team, role, jersey_number, mname = ''):
        """Initialize the attributes to describe a player."""
        self.fname = fname
        self.lname = lname
        self.team = team
        self.role = role
        self.jersey_number = jersey_number
        self.point_default = 0 #does need to be in the parentheses
        self.mname = mname

    def get_name(self):
        """Return player's name: first and last"""
        full_name = self.fname + self.lname
        if self.mname:
            full_name = self.fname.title() + ' ' + self.mname.title() + ' ' + self.lname.title()
        else:
            full_name = self.fname.title() + ' ' + self.lname.title()
        return full_name.title()

    def update_point(self, points):
        """Set the point to a given value."""
        """Reject if point is less than 0"""
        if points >= 0:
            self.point_default =  points
        else:
            print("The player cannot score negative points!")

    def increment_two_pointers(self, two_points):
        two_points = 2
        self.point_default += two_points


    def show_point(self):
        """Print a statement showing the player's score."""
        print(Player.get_name(self) + " has " + str(self.point_default) + " points.")

player_1 = Player('Kaitlyn', 'Chen', 'Valkyries', 'point guard', 2)
print(player_1.get_name())
player_1.show_point()

#changing attribute directly
player_1.point_default = 3
player_1.show_point()

#modifying an attribute's value through a method
player_1.update_point(7)
player_1.show_point()
player_1.update_point(-1)
player_1.show_point()

player_1.increment_two_pointers(4) #prediction is that it will add two points two times
player_1.show_point()