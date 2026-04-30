"""
Udemy 100 Days of Code: Day 19
TBD
"""

from d019 import d019l140, d019l143


def main(file_name):
    """Entry function for Day ddd code"""
    print("D019 running!")
    handlers = {
        "d019l140.py": d019l140.main,
        "d019l143.py": d019l143.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
