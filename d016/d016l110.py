"""
50 Days of Code, Day 16, Lesson 110
OOP
"""

from turtle import Turtle, Screen
import prettytable


def main():
    """
    Code for Day 16 Lesson 110
    OOP - Turtle
    """
    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("green")
    timmy.forward(50)
    for _ in range(6):
        timmy.left(60)
        timmy.forward(50)
    for _ in range(6):
        for _ in range(5):
            timmy.right(60)
            timmy.forward(50)
        for _ in range(5):
            timmy.left(60)
            timmy.forward(50)

    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()


if __name__ == "__main__":
    main()
