"""
Car manager class for turtle game
"""

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
RIGHT_EDGE = 280
LEFT_EDGE = -280


class CarManager(Turtle):
    """CarManager class for turtle game"""

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        """create a new car"""
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setposition(RIGHT_EDGE, random.randint(-240, 240))
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        """move each of the cars forward"""
        # go through the list of cars backwards so removing a car doesn't mess up the loop
        for car_num in range(len(self.cars) - 1, -1, -1):
            car = self.cars[car_num]
            car.forward(self.car_speed)
            if car.xcor() <= LEFT_EDGE:
                car.hideturtle()
                del self.cars[car_num]

    def check_for_collision(self, turtle_y_pos):
        """check if any of the cars has hit the turtle"""
        # check if the car is at xpos between -30 and 30, and a ypos within 20 of the turtle
        # use a filter
        collision = False
        result = list(
            filter(
                lambda c: abs(c.xcor()) <= 30 and abs(turtle_y_pos - c.ycor()) <= 20,
                self.cars,
            )
        )
        for car in result:
            print(f"{turtle_y_pos=}, {car.ycor()=}, {car.xcor()=}")
            car.color("silver")
            collision = True
        return collision

    def speed_up_cars(self):
        """increase the speed of the cars by MOVE_INCREMENT"""
        self.car_speed += MOVE_INCREMENT
        print(f"{self.car_speed=}")

    # def clear_cars(self):
    #     """clear the list of cars and add one new car"""
    #     for car in self.cars:
    #         car.hideturtle()
    #     self.cars = []
    #     self.new_car()
