"""
Player class for turtle game}
"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Player class for turtle game}"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.move_to_starting_position()

    def move(self):
        """move the player forward by MOVE_DISTANCE"""
        self.sety(self.ycor() + MOVE_DISTANCE)

    def crossed_road(self):
        """return True if player has passed the finish line, false otherwise"""
        return self.ycor() >= FINISH_LINE_Y

    def move_to_starting_position(self):
        """move the turtle to the starting position"""
        self.setposition(STARTING_POSITION)
