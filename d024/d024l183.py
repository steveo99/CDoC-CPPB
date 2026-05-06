"""
100 Days of Code, Day 24, Lesson 183
<description>
"""


def read_file(file_name: str):
    """read a file"""
    with open(file_name, encoding="utf-8") as file:
        contents = file.read()
        print(contents)


def write_file(file_name: str):
    """write to a file"""
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write("new text")


def append_file(file_name: str):
    """append to a file"""
    with open(file_name, mode="a", encoding="utf-8") as file:
        file.write("\nmore text")


def main():
    """
    Code for Day 24 Lesson 183
    reading from and and writing to files
    """
    read_file("d024/my_file.txt")
    write_file("d024/new_file.txt")
    read_file("d024/new_file.txt")
    append_file("d024/my_file.txt")
    read_file("d024/my_file.txt")
    read_file(r"c:\users\steve\onedrive\desktop\desktop_file.txt")
    write_file(r"c:\users\steve\onedrive\desktop\desktop_file.txt")
    append_file(r"c:\users\steve\onedrive\desktop\desktop_file.txt")
    read_file(r"c:\users\steve\onedrive\desktop\desktop_file.txt")


if __name__ == "__main__":
    main()
