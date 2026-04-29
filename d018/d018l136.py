"""
100 Days of Code, lesson 136
use turtle to display the colors in the color palate
"""

import turtle
import colorgram

rgb_colors = [
    (40, 45, 50),
    # (226, 223, 218),
    # (221, 223, 227),
    # (220, 226, 222),
    # (229, 220, 224),
    (164, 78, 43),
    (129, 32, 48),
    (218, 211, 109),
    (188, 168, 107),
    (58, 26, 34),
    (166, 158, 50),
    (60, 102, 137),
    (146, 60, 81),
    (144, 170, 181),
    (44, 37, 29),
    (123, 190, 168),
    (27, 40, 36),
    (53, 108, 77),
    (42, 48, 105),
    (184, 89, 133),
    (143, 33, 28),
    (86, 170, 75),
    (182, 149, 161),
    (17, 94, 67),
    (215, 84, 51),
    (159, 210, 194),
    (224, 205, 15),
    (77, 150, 157),
    (222, 173, 183),
    (236, 172, 162),
]


def extract_colors(image: str, num_colors: int):
    """
    use the colorgram package to extract num_colors colors from image
    """
    extracted_colors = []
    colors = colorgram.extract(image, num_colors)
    # print(colors)
    for color in colors:
        # print(color)
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        extracted_colors.append((r, g, b))
    return extracted_colors


def display_colors(t: turtle.Turtle, colors):
    """display the colors"""
    t.hideturtle()
    saved = t.pen()
    t.penup()
    x_dot, x, y = -300, -250, 300
    for color in colors:
        t.setposition(x_dot, y)
        t.dot(20, color)
        t.setposition(x, y - 7)
        t.write(color)
        y -= 20
    t.pen(saved)


def main():
    """
    Code for Day 18 Lesson 136
    extract colors using colorgram
    """

    # extract colors from image
    extracted_colors = extract_colors("d018/image.jpg", 30)
    print(extracted_colors)

    turtle.colormode(255)  # pylint: disable=no-member
    tim = turtle.Turtle()
    display_colors(tim, rgb_colors)

    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
