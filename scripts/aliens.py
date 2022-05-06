class Alien:
    health = 3

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def hit(self):
        if self.health > 0:
            self.health -= 1
