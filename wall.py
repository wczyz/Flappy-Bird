#Wall class

from graphics import *
from settings import *

class Wall:

    def __init__(self, x, y, space, color, win):
        """Constructor setting wall's initial position and color."""

        self.x = x
        self.y = y
        self.space = space

        self.upRect = Rectangle(Point(x, 0), Point(x + WALL_WIDTH, y))
        self.downRect = Rectangle(Point(x, y + space), Point(x + WALL_WIDTH, WIN_Y))

        self.upRect.setFill(color)
        self.downRect.setFill(color)

        self.window = win

    def update(self):
        """Function moving the wall accordingly to the game speed."""

        self.x += GAME_SPEED
        self.upRect.move(GAME_SPEED, 0)
        self.downRect.move(GAME_SPEED, 0)