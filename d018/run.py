"""
Udemy 100 Days of Code: Day 18
Turtle and GUI
"""

from d018 import d018l129, d018l136, d018l137


def main(file_name):
    """Entry function for Day ddd code"""
    print("D018 running!")
    handlers = {
        "d018l129.py": d018l129.main,
        "d018l136.py": d018l136.main,
        "d018l137.py": d018l137.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
