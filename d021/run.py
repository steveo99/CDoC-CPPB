"""
Udemy 100 Days of Code: Day ddd
<description>
"""

from d021 import d021l154


def main(file_name):
    """Entry function for Day ddd code"""
    print("D021 running!")
    handlers = {
        "d021l154.py": d021l154.main,  # pylint: disable=no-member
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
