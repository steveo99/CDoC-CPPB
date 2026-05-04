"""
100 Days of Code, Day 22, Lesson 161
Pong arcade game
"""

from turtle import Screen
from d022.paddle import Paddle
from d022.ball import Ball
from d022.scoreboard import Scoreboard

# board coordinates
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LEFT = SCREEN_WIDTH * -0.5 + 40
RIGHT = SCREEN_WIDTH * 0.5 - 40
TOP = SCREEN_HEIGHT * 0.5 - 20
BOTTOM = SCREEN_HEIGHT * -0.5 + 20


def main():
    """
    Code for Day 22 Lesson 161 - 168
    Pong arcade game
    """

    game_on = True

    def end_the_game():
        nonlocal game_on
        game_on = False

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle(RIGHT)
    l_paddle = Paddle(LEFT)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")
    screen.onkey(end_the_game, "q")

    while game_on:
        screen.update()
        ball.move()
        ball_x = ball.xcor()
        ball_y = ball.ycor()

        # detect colision with top or bottom
        if ball_y >= TOP or ball_y <= BOTTOM:
            ball.bounce_y()

        # detect colision with paddles
        # r_y_diff and l_y_diff hold how far the ball hit from the center of the paddle
        # used later to adjust the steepness of the ball path
        r_y_diff = ball_y - r_paddle.ycor()
        l_y_diff = ball_y - l_paddle.ycor()

        if (ball_x >= RIGHT and abs(r_y_diff) <= 60) or (
            ball_x <= LEFT and abs(l_y_diff) <= 60
        ):
            # hit one of the paddles
            # adjust the ball's y_move
            if ball_x >= RIGHT:
                ball.adjust_y_move(int(round(r_y_diff / 15)))
            else:
                ball.adjust_y_move(int(round(l_y_diff / 15)))
            # reverse the ball direction
            ball.bounce_x()
            continue

        # detect moving off the right edge
        if ball_x >= RIGHT:
            scoreboard.l_point()
            ball.reset_position()

        if ball_x <= LEFT:
            scoreboard.r_point()
            ball.reset_position()

    screen.exitonclick()


if __name__ == "__main__":
    main()
