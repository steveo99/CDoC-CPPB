"""
100 Days of Code, Day 9
Dictionaries, Nesting and the Secret Auction
"""

from d009 import d009ex9, d009l069, d009l070


def main(file_name):
    """Entry function for Day 9 code"""

    print("D009 running!")
    handlers = {
        "d009ex9.py": d009ex9.main,
        "d009l069.py": d009l069.main,
        "d009l070.py": d009l070.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
