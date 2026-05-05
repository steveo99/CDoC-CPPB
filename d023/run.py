"""
Udemy 100 Days of Code: Day 23
Turtle game
"""

from d023 import turtle_game


def main(file_name):
    """Entry function for Day ddd code"""
    print("D023 running!")
    handlers = {
        "turtle_game.py": turtle_game.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
