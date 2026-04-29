"""
100 Days of Code, Day 18, Lesson 136
The Hirst Painting Project
"""

import random
import turtle
from turtle import Turtle, Screen

rgb_colors = [
    (40, 45, 50),
    (164, 78, 43),
    (129, 32, 48),
    (218, 211, 109),
    (188, 168, 107),
    (58, 26, 34),
    (166, 158, 50),
    (60, 102, 137),
    (146, 60, 81),
    (144, 170, 181),
    (44, 37, 29),
    (123, 190, 168),
    (27, 40, 36),
    (53, 108, 77),
    (42, 48, 105),
    (184, 89, 133),
    (143, 33, 28),
    (86, 170, 75),
    (182, 149, 161),
    (17, 94, 67),
    (215, 84, 51),
    (159, 210, 194),
    (224, 205, 15),
    (77, 150, 157),
    (222, 173, 183),
    (236, 172, 162),
]


def print_hirst_painting(t: Turtle, colors: list[tuple[int, int, int]]):
    """
    print a 10 by 10 hirst picture
    """
    t.hideturtle()
    saved = t.pen()
    # dot works even with penup, so I can put penup, and just leave it there.
    t.penup()
    x_start = -250
    y_start = 250
    for row in range(11):
        for col in range(11):
            x = x_start + 50 * col
            y = y_start - 50 * row
            t.setposition(x, y)
            color = random.choice(colors)
            t.dot(20, color)
    t.pen(saved)


def main():
    """
    Code for Day 18 Lesson 137
    The Hirst Painting Project
    """

    turtle.colormode(255)  # pylint: disable=no-member
    tim = Turtle()
    tim.speed(0)
    print_hirst_painting(tim, rgb_colors)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
