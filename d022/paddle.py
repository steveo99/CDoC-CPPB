"""
Paddle class for pong game
"""

from turtle import Turtle


class Paddle(Turtle):
    """Paddle class for Pong game"""

    def __init__(self, x_coordinate: int):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition((x_coordinate, 0))
        self.speed("fastest")

    def up(self):
        """move the paddle up 20"""
        self.sety(self.ycor() + 20)

    def down(self):
        """move the paddle down 20"""
        self.sety(self.ycor() - 20)
