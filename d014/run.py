"""
Udemy 100 Days of Code: Day 14
Higher Lower Project
"""

from d014 import d014l102


def main(file_name):
    """Entry function for Day ddd code"""
    print("D014 running!")
    handlers = {"d014l102.py": d014l102.main}
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
