"""
100 Days of Code, Day 20, Lesson 146
tbd
"""

from turtle import Screen, Turtle
import time


def create_segment(x: int, y: int):
    """create a turtle segment centered at x, y"""
    s = Turtle("square")
    s.color("white")
    s.speed(0)
    s.penup()
    s.setposition(x, y)
    return s


def move_up(t: Turtle):
    """turn turtle heading up"""
    t.setheading(90)


def move_left(t: Turtle):
    """turn turtle heading left"""
    t.setheading(180)


def move_down(t: Turtle):
    """turn turtle heading dpwm"""
    t.setheading(270)


def move_right(t: Turtle):
    """turn turtle heading left"""
    t.setheading(0)


def main():
    """
    Code for Day 20 Lesson 146
    tbd
    """
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.listen()
    segments: list[Turtle] = []
    num_segments = 3
    for n in range(num_segments):
        s = create_segment(n * -20, 0)
        segments.append(s)

    screen.onkey(lambda: move_up(segments[0]), "Up")
    screen.onkey(lambda: move_left(segments[0]), "Left")
    screen.onkey(lambda: move_down(segments[0]), "Down")
    screen.onkey(lambda: move_right(segments[0]), "Right")

    game_on = True
    delay = 0.1
    move = 0
    while game_on:
        move += 1
        tail_pos = segments[-1].position()
        for segment_num in range(num_segments - 1, 0, -1):
            tp_new = segments[segment_num - 1].position()
            segments[segment_num].goto(tp_new)

        time.sleep(delay)
        segments[0].forward(20)
        screen.update()
        if move % 15 == 0:
            segments.append(create_segment(tail_pos[0], tail_pos[1]))
            num_segments += 1
            print(f"{num_segments=}")
        if move % 70 == 0:
            delay *= 0.9
            print(f"{delay=}")
        # check for hit wall
        if abs(segments[0].xcor()) >= 280 or abs(segments[0].ycor()) >= 280:
            print("Hit wall.")
            game_on = False
        # check if hit tail
        head_x = segments[0].position()[0]
        head_y = segments[0].position()[1]
        for segment_num in range(1, num_segments):
            if (
                segments[segment_num].position()[0] == head_x
                and segments[segment_num].position()[1] == head_y
            ):
                print("Hit tail.")
                game_on = False
        time.sleep(delay)

    screen.exitonclick()


if __name__ == "__main__":
    main()
