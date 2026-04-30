"""
100 Days of Code, Day 19, Lesson 143
TBD
"""

import random
from turtle import Turtle, Screen


def main():
    """
    Code for Day 19 Lesson 143
    TBD
    """
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
    )
    colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "purple",
    ]
    turtles: list[Turtle] = []
    for i in range(6):
        t = Turtle("turtle")
        t.color(colors[i])
        t.penup()
        t.goto(x=-230, y=-125 + 50 * i)
        turtles.append(t)

    race_over = False
    while not race_over:
        distance = random.randint(1, 10)
        t = random.randint(0, 5)
        turtles[t].forward(distance)
        if turtles[t].xcor() >= 230:
            race_over = True
            winner = turtles[t].pencolor()
            outcome = "won" if winner == user_bet else "lost"
            print(f"You've {outcome}! The {winner} turtle is the winner!")

    if winner == user_bet:
        print("You were right!")

    screen.exitonclick()


if __name__ == "__main__":
    main()
