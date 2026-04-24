"""
Udemy 100 Days of Code: Day 15
Coffee Machine Project
"""

from d015 import d015l105


def main(file_name):
    """Entry function for Day ddd code"""
    print("Dddd running!")
    handlers = {
        "d015l105.py": d015l105.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
