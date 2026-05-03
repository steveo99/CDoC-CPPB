"""
100 Days of Code, Day 021, Lesson 154
Snake game using OOP part 2
"""

from turtle import Screen
import time
from d021.snake import Snake
from d021.food import Food
from d021.scoreboard import Scoreboard


def main():
    """
    Code for Day 21 Lesson 154
    snake program using OOP part 2
    """
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.listen()
    screen.tracer(0)
    delay = 0.12
    snake = Snake(3)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    food = Food()
    scoreboard = Scoreboard()

    game_on = True
    while game_on:
        screen.update()
        time.sleep(delay)

        snake.move()

        # check for collision with food
        if snake.head.distance(food) < 15:
            print("nom nom nom")
            scoreboard.increase_score()
            food.refresh()
            snake.extend()

        if snake.move_number % 100 == 0:
            delay *= 0.9
            print(f"{snake.move_number=}: {delay=}")

        if snake.check_for_game_over():
            game_on = False
            scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
