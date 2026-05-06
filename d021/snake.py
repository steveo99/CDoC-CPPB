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
            add_position = (i * -20, 0)
            self.add_segment(add_position)
        # self.print_snake()

    def add_segment(self, position: tuple[int, int]):
        """create a turtle segment centered at position"""
        s = Turtle("square")
        s.color("white")
        s.speed("fastest")
        s.penup()
        s.setposition(position)
        self.segments.append(s)

    def extend(self):
        """add a new segment to the snake"""
        tail_pos = self.segments[-1].position()
        self.add_segment(tail_pos)
        print(f"Segments={len(self.segments)}")

    def reset(self):
        """reset snake"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake(3)
        self.head = self.segments[0]
        self.move_number = 0

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
        for segment_num in range(num_segments - 1, 0, -1):
            tp_new = self.segments[segment_num - 1].position()
            self.segments[segment_num].goto(tp_new)

        self.head.forward(MOVE_DISTANCE)
        # self.print_snake()

    def print_snake(self):
        """print the coordinates of the snake segments"""
        for i, segment in enumerate(self.segments):
            print(f"{i=}, ({segment.xcor()}, {segment.ycor()})")

    def check_for_game_over(self):
        """check if the game is over"""
        # check if hit the wall
        if (
            abs(self.head.xcor()) > self.grid_width / 2 - 10
            or abs(self.head.ycor()) > self.grid_height / 2 - 10
        ):
            print("Hit wall")
            return True
        # check if hit the tail
        for segment in self.segments[1:]:
            if self.head.distance(segment) <= 10:
                print(f"segment position: {segment.position()}")
                print("Hit tail")
                self.print_snake()
                return True
        return False
