"""
Udemy 100 Days of Code: Day 16b
OOP Coffee Machine
"""

from d016b import d016bl113


def main(file_name):
    """Entry function for Day ddd code"""
    print("D016b running!")
    handlers = {
        "d016bl113.py": d016bl113.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
