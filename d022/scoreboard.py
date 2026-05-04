"""Scoreboard class for the pong game"""

from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard class for Pong game"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """show the score of the left and right player"""
        self.clear()
        self.setposition(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.setposition(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        """update the left player score and update the scoreboard"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """update the right player score and update the scoreboard"""
        self.r_score += 1
        self.update_scoreboard()
