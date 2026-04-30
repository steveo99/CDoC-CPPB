"""
100 Days of Code, Day 019, Lesson 140
Etch-a-Sketch program
"""

from turtle import Turtle, Screen


def move_forwards(t: Turtle):
    """move turtle t forward 10 steps"""
    t.forward(10)


def move_backwards(t: Turtle):
    """move turtle t backward 10 steps"""
    t.backward(10)


def counter_clockwise(t: Turtle):
    """turn turtle t counter clockwise 10 degrees"""
    t.left(10)


def clockwise(t: Turtle):
    """turn turtle t clockwise 10 degrees"""
    t.right(10)


def clear(t: Turtle):
    """clear turtle t drawings, move back to home"""
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def main():
    """
    Code for Day 19 Lesson 140
    Etch-a-Sketch program
    """

    tim = Turtle()
    screen = Screen()

    screen.listen()
    screen.onkey(lambda: move_forwards(tim), "w")
    screen.onkey(lambda: move_backwards(tim), "s")
    screen.onkey(lambda: counter_clockwise(tim), "a")
    screen.onkey(lambda: clockwise(tim), "d")
    screen.onkey(lambda: clear(tim), "c")

    screen.exitonclick()


if __name__ == "__main__":
    main()
