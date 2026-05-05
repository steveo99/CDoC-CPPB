"""
Scoreboard class for turtle game
"""

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Scoreboard class for turtle game"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("green")
        self.penup()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """show the score of the left and right player"""
        self.clear()
        self.setposition(-100, 200)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def increment_level(self):
        """increment the scoreboard level"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """show Game Over"""
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)
