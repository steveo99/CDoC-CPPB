"""
Udemy 100 Days of Code: Day 16
day 16 - OOP
"""

from d016 import d016l110, d016l112


def main(file_name):
    """Entry function for Day ddd code"""
    print("D016 running!")
    handlers = {
        "d016l110.py": d016l110.main,
        "d016l112.py": d016l112.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
