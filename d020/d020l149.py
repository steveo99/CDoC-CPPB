"""
100 Days of Code, Day 020, Lesson 149
Snake game using OOP
"""

from turtle import Screen
import time
from d020.snake import Snake


def direction_up(snake: Snake):
    """change the direction of the snake to up"""
    snake.up()


def direction_down(snake: Snake):
    """change the direction of the snake to up"""
    snake.down()


def direction_left(snake: Snake):
    """change the direction of the snake to up"""
    snake.left()


def direction_right(snake: Snake):
    """change the direction of the snake to up"""
    snake.right()


# def change_direction(snake: Snake, direction: str):
#     """change the direction of the snake"""
#     snake.change_direction(new_direction=direction)


def main():
    """
    Code for Day 20 Lesson 149
    snake program using OOP
    """
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.listen()
    screen.tracer(0)
    delay = 0.1
    snake = Snake(3)
    screen.onkey(lambda: direction_up(snake), "Up")
    screen.onkey(lambda: direction_down(snake), "Down")
    screen.onkey(lambda: direction_left(snake), "Left")
    screen.onkey(lambda: direction_right(snake), "Right")

    move = 0
    game_on = True
    while game_on:
        screen.update()
        time.sleep(delay)

        move = snake.move()
        if move % 100 == 0:
            delay *= 0.95
            print(f"{move=}: {delay=}")

        game_on = not snake.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
