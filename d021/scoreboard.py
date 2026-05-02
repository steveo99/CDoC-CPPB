"""Scoreboard class for the snake game"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    """Scoreboard class for the snake game"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score and update the scoreboard"""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """update the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """display the game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
