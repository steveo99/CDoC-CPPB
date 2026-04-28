"""
Udemy 100 Days of Code: Day ddd
<description>
"""

from d017q import d017ql120


def main(file_name):
    """Entry function for Day ddd code"""
    print("D17q running!")
    handlers = {
        "d017ql120.py": d017ql120.main,
    }
    if handler := handlers.get(file_name):
        handler()
    else:
        print(f"invalid {file_name=}")
