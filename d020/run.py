"""
Udemy 100 Days of Code: Day 20
snake game
"""

from d020 import d020l147, d020l149


def main(file_name):
    """Entry function for Day ddd code"""
    print("Dddd running!")
    handlers = {
        "d020l147.py": d020l147.main,
        "d020l149.py": d020l149.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
