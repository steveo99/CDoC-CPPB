"""
Snake class
"""

from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Snake class
    """

    def __init__(
        self, num_segments: int, grid_width: int = 600, grid_height: int = 600
    ):
        self.segments: list[Turtle] = []
        self.direction = 0
        self.create_snake(num_segments)
        self.move_number = 0
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.head = self.segments[0]

    def create_snake(self, num_segments: int):
        """create the initial snake"""
        for i in range(num_segments):
            segment = self.create_segment(i * -20, 0)
            self.segments.append(segment)

    def create_segment(self, x: int, y: int):
        """create a turtle segment centered at x, y"""
        s = Turtle("square")
        s.color("white")
        s.speed(0)
        s.penup()
        s.setposition(x, y)
        return s

    # def change_direction(self, new_direction: str):
    #     """set the new direction of the snake"""
    #     directions = {"up": 90, "left": 180, "down": 270, "right": 0}
    #     self.segments[0].setheading(directions[new_direction.lower()])

    def up(self):
        """turn the snake up if not going down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """turn the snake down if not going up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """turn the snake left if not going right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """turn the snake right if not going left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        """do the next move in the snake game"""
        self.move_number += 1

        num_segments = len(self.segments)
        tail_pos = self.segments[-1].position()
        for segment_num in range(num_segments - 1, 0, -1):
            tp_new = self.segments[segment_num - 1].position()
            self.segments[segment_num].goto(tp_new)

        self.head.forward(MOVE_DISTANCE)

        if self.move_number % 15 == 0:
            self.segments.append(self.create_segment(tail_pos[0], tail_pos[1]))
            print(f"{len(self.segments)=}")

        return self.move_number

    def game_over(self):
        """check if the game is over"""
        # check if hit the wall
        if (
            abs(self.head.xcor()) > self.grid_width / 2 - 10
            or abs(self.head.ycor()) > self.grid_height / 2 - 10
        ):
            print("Hit wall")
            return True
        # check if hit the tail
        head_x = round(self.head.xcor(), 0)
        head_y = round(self.head.ycor(), 0)
        for segment_num in range(1, len(self.segments)):
            tail_x = round(self.segments[segment_num].xcor(), 0)
            tail_y = round(self.segments[segment_num].ycor(), 0)
            # print(
            #     f"{self.move_number=} {segment_num=}: {head_x=},{head_y=},{tail_x=},{tail_y=},"
            # )
            if head_x == tail_x and head_y == tail_y:
                print("Hit tail.")
                return True
        return False
