"""
Food class for the snake game"""

from turtle import Turtle
import random


class Food(Turtle):
    """
    Food class for the snake game
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """put the food at a random location in the window"""
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
