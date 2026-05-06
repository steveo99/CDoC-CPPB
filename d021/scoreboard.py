"""Scoreboard class for the snake game"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


def read_high_score():
    """read the high score from data.txt"""
    with open("d021/data.txt", encoding="utf-8") as file:
        contents = file.read()
    return int(contents)


def write_high_score(new_high_score: int):
    """read the high score from data.txt"""
    with open("d021/data.txt", "w", encoding="utf-8") as file:
        file.write(str(new_high_score))


class Scoreboard(Turtle):
    """Scoreboard class for the snake game"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
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
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        """reset scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """display the game over message"""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
