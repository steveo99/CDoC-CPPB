"""
100 Days of Code, Day 16, Lesson 112
using PrettyTable
"""

from prettytable import PrettyTable


def main():
    """
    Code for Day 16 Lesson 112
    using PrettyTable
    """
    table = PrettyTable()
    table.field_names = ["Pokemon Name", "Type"]
    table.add_row(["Pikachu", "Electric"])
    table.add_row(["Squirtle", "Water"])
    table.add_row(["Charmander", "Fire"])
    print(table)
    print()
    table = PrettyTable()
    table.add_column(
        "Pokemon Name",
        [
            "Pikachu",
            "Squirtle",
            "Carmander",
        ],
    )
    table.add_column(
        "Type",
        [
            "Electric",
            "Water",
            "Fire",
        ],
    )
    table.align = "l"
    print(table)


if __name__ == "__main__":
    main()
