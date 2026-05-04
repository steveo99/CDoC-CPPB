"""
Udemy 100 Days of Code: Day 22
Pong game
"""

from d022 import pong_game


def main(file_name):
    """Entry function for Day ddd code"""
    print("022 running!")
    handlers = {
        "pong_game.py": pong_game.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
