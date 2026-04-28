"""
Udemy 100 Days of Code: Day 17
Create your own classes in Python
"""

from d017 import d017l117


def main(file_name):
    """Entry function for Day ddd code"""
    print("D17 running!")
    handlers = {
        "d017l117.py": d017l117.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
