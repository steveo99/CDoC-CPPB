"""
Udemy 100 Days of Code: Day 24
reading from and writing to files
"""

from d024 import d024l183


def main(file_name):
    """Entry function for Day ddd code"""
    print("D024 running!")
    handlers = {
        "d024l183.py": d024l183.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
