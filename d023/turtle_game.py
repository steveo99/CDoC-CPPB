"""
100 Days of Code, Day 23, Lesson 171
Turtle game
"""

import time
import random
from turtle import Screen
from d023.player import Player
from d023.car_manager import CarManager
from d023.scoreboard import Scoreboard

# board coordinates
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def main():
    """
    Code for Day 23 Lesson 171
    Turtle game
    """

    game_on = True

    def end_the_game():
        nonlocal game_on
        game_on = False

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Turtle")
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    car_manager.new_car()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.move, "Up")
    screen.onkey(end_the_game, "q")

    new_car_frequency = 15.0
    num_moves = 0
    while game_on:
        num_moves += 1
        time.sleep(0.1)
        screen.update()
        car_manager.move_cars()
        if car_manager.check_for_collision(player.ycor()):
            game_on = False
            scoreboard.game_over()
            screen.update()

        if random.randint(0, int(round(new_car_frequency, 0))) == 0:
            car_manager.new_car()

        if player.crossed_road():
            scoreboard.increment_level()
            player.move_to_starting_position()
            # car_manager.clear_cars()
            new_car_frequency = new_car_frequency * 0.8
            car_manager.speed_up_cars()
            print(f"{new_car_frequency=}")

        # if scoreboard.level == 12:
        #     scoreboard.game_over()
        #     game_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
