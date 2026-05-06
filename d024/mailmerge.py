"""
100 Days of Code, Day 24, Lesson nnn
<description>
"""

PLACEHOLDER = "[name]"


def read_file_lines(filename: str):
    """open a file, return the contents as a list of lines"""
    with open(filename, encoding="utf-8") as file:
        contents = file.readlines()
    return contents


def read_file(filename: str):
    """open a file, return the contents as a single string"""
    with open(filename, encoding="utf-8") as file:
        contents = file.read()
    return contents


def write_file(filename: str, contents: str):
    """write contents to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(contents)


def main():
    """
    Code for Day ddd Lesson 186
    mailmerge program
    """

    # Create a letter using starting_letter.txt
    # for each name in invited_names.txt
    # Replace the [name] placeholder with the actual name.
    # Save the letters in the folder "ReadyToSend".

    # Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

    # get the starting letter
    starting_letter = read_file("d024/Input/Letters/starting_letter.txt")
    # get the names list
    names_list = read_file_lines("d024/Input/Names/invited_names.txt")

    # print(starting_letter)
    # print(names_list)
    for name in names_list:
        name = name.strip().replace("\n", "")
        # print(name)
        new_letter = starting_letter.replace(PLACEHOLDER, name)
        new_letter_filename = f"d024/Output/ReadyToSend/letter_for_{name}.txt"
        write_file(new_letter_filename, new_letter)


if __name__ == "__main__":
    main()
