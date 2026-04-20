"""Udemy 100 Days of Code: Day 10"""

from d010 import d010l076


def main(file_name):
    """Entry function for Day 10 code"""
    print("D010 running!")
    handlers = {
        "d010l076.py": d010l076.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
