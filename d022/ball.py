"""
Ball class for the Pong game
"""

from turtle import Turtle
import time

STARTING_MOVE_SPEED = 0.1
STARTING_X_MOVE = 10
STARTING_Y_MOVE = 4


class Ball(Turtle):
    """Ball class for the Pong game"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = STARTING_X_MOVE
        self.y_move = STARTING_Y_MOVE
        self.move_speed = STARTING_MOVE_SPEED

    def move(self):
        """
        move the x, y position of the ball by the x_move and y_move values
        """

        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.setposition((x_pos, y_pos))
        time.sleep(self.move_speed)

    def bounce_y(self):
        """bounced of top or bottom, reverse the y_move"""
        self.y_move *= -1

    def adjust_y_move(self, adjustment: int):
        """
        adjust the amount of the y_move by adjustment
        this changes the steepness of the ball's path
        """
        self.y_move += adjustment

    def bounce_x(self):
        """bounced of the paddle, reverse the x_move, increase the speed"""
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        """start a new point, reset the orientation"""
        # reverse the direction of the ball
        self.bounce_x()
        self.goto(0, 0)
        self.move_speed = STARTING_MOVE_SPEED
        self.y_move = STARTING_Y_MOVE
