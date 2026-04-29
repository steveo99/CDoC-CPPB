"""
100 Days of Code, Day 18, Lesson 129
Turtle and GUI
"""

import random
from turtle import Turtle, Screen


def set_pos_dir(t: Turtle, x: float, y: float, heading: float = 0):
    """set turtles position at x, y with a heading of heading"""
    saved = t.pen()
    t.penup()
    t.setpos(x, y)
    t.setheading(heading)
    t.pen(pendown=saved["pendown"])


def square(t: Turtle, steps: int):
    """draw a square"""
    saved = t.pen()
    t.pendown()
    for _ in range(4):
        t.forward(steps)
        t.right(90)
    t.pen(saved)


def dashed_line(
    t: Turtle, line_len: float = 10, gap_len: float = 10, num_dashes: int = 50
):
    """draw a dashed line,"""
    saved = t.pen()
    for _ in range(num_dashes):
        t.pendown()
        t.forward(line_len)
        t.penup()
        t.forward(gap_len)
    t.pen(saved)


def random_color():
    """return a random color rgb"""
    return (
        random.randint(0, 255) / 255,
        random.randint(0, 255) / 255,
        random.randint(0, 255) / 255,
    )


def draw_shape(t: Turtle, sides: int, side_len: float, color: str):
    """
    draw an n sided shape with given side length in the specified color
    if color is "random", pick a random color
    """
    saved = t.pen()
    turn_angle = 360 / sides
    if color == "random":
        t.pencolor(random_color())
    else:
        t.pencolor(color)
    for _ in range(sides):
        t.right(turn_angle)
        t.forward(side_len)
    t.pen(saved)


def random_walk(t: Turtle, walk_len: int, walks: int, line_width: float):
    """
    have the turtle take a random walk
    each walk of lenght walk_len
    take walks walks
    """
    directions = [0, 90, 180, 270]
    saved = t.pen()
    t.pendown()
    t.pensize(line_width)
    t.speed(0)
    for _ in range(walks):
        t.pencolor(random_color())
        t.setheading(random.choice(directions))
        t.forward(walk_len)
    t.pen(saved)


def draw_circle(t: Turtle, x: float, y: float, radius: float, color: str):
    """draw a circle with radius radius in color color centered around x, y"""
    saved = t.pen()
    x, y = t.position()
    t.penup()
    t.setposition(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)
    t.penup()
    t.setposition(x, y)
    t.pen(saved)


def spirograph(t: Turtle, radius: float, num_circles: int):
    """draw num_circles with radius radius in random colors"""
    saved = t.pen()
    save_heading = t.heading()
    heading = 0.0
    increment = 360 / num_circles
    t.speed(0)
    for _ in range(num_circles):
        heading += increment
        t.setheading(heading)
        t.color(random_color())
        t.circle(radius)
    t.setheading(save_heading)
    t.pen(saved)


def main():
    """
    Code for Day 18 Lesson 228
    Turtle and GUI
    """
    tim = Turtle()
    tim.speed(10)

    # sdraw a square
    set_pos_dir(tim, -400, 380)
    square(tim, 40)

    # draw a dashed line
    set_pos_dir(tim, -400, 320)
    dashed_line(tim, 8, 2, 20)

    # draw 3, 4, 5, 6, 7, 8, 9, 10 sided figures in random colors
    set_pos_dir(tim, -200, 300)
    tim.forward(50)
    set_pos_dir(tim, -300, 300)
    for sides in range(3, 11):
        draw_shape(tim, sides, 60, "random")
    set_pos_dir(tim, -200, 290)
    tim.forward(50)

    # random walk
    x, y = -200, 100
    set_pos_dir(tim, x, y)
    draw_circle(tim, x, y, 10, "red")
    random_walk(tim, 15, 100, 4)
    x, y = -50, 100
    set_pos_dir(tim, x, y)
    draw_circle(tim, x, y, 10, "red")
    random_walk(tim, 15, 100, 6)
    x, y = 100, 100
    set_pos_dir(tim, x, y)
    draw_circle(tim, x, y, 10, "red")
    random_walk(tim, 15, 100, 8)
    set_pos_dir(tim, -200, 280)
    tim.forward(50)

    # spirograph
    set_pos_dir(tim, 0, -150)
    spirograph(tim, 100, 90)
    set_pos_dir(tim, -200, 270)
    tim.forward(50)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
