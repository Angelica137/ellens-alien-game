class Alien:
    health = 3
    counter = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        Alien.counter += 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def hit(self):
        """
        Reduces alien's health by 1 each time it is hit. 
        Health does not go below 0
        """
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        """
        Returns true if the alien is alive: health is greater than 0
        Returns False is alien is dead
        """
        return self.health > 0

    def teleport(self, x_coordinate: int, y_coordinate: int):
        """
        Changes the location of the alien to the coordinates passes.
        God knows where these come from
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_bject):
        """
        🔥 You still need to do this
        Returns True when a collision has occurred
        """
        pass

    def total_aliens_created(self):
        """
        Returns the total number of instances of an Alien created during 
        the session
        """
        return Alien.counter


def new_aliens_collection(locations: list):
    """
    Takes a list of coordinate pairs and returns a list of Alien objects
    """
    aliens = [Alien(location[0], location[1]) for location in locations]
    return aliens


"""
a = [Alien(-2, 6)]
print(a[0].total_aliens_created())
"""
