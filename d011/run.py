"""Udemy 100 Days of Code: Day 11"""

from d011 import d011l079


def main(file_name):
    """Entry function for Day 11 code"""
    print("d011 running!")
    handlers = {
        "d011l079.py": d011l079.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
