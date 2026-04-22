"""
Udemy 100 Days of Code: Day 12
Exercise 11: Prime Number Checker
"""

from d012 import d012ex11, d012l092


def main(file_name):
    """Entry function for Day ddd code"""
    print("D012 running!")
    handlers = {
        "d012ex11.py": d012ex11.main,
        "d012l092.py": d012l092.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
