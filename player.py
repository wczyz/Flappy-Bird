#Player class

from graphics import *
from settings import *

class Player:

    def __init__ (self, x, y , color, win):
        """Constructor setting player's color and initial position."""

        self.x = x
        self.y = y
        self.color = color
        self.position = Point(x, y)
        self.velocity = 0                           #Player's current velocity. Positive velocity is directed downwards, negative upwards.
        self.window = win
        self.body = Circle(self.position, PLAYER_SIZE)
        self.body.setFill(color)

    def update(self):
        """Function that moves the player with respect to the velocity and updates velocity."""

        self.body.move(0, self.velocity)
        self.y += self.velocity
        self.velocity += GRAVITY