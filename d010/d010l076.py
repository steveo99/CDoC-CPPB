"""100 Days of Code, Day 10, calculator project"""

from d010.art import LOGO


def add(n1, n2):
    """add 2 numbers"""
    return n1 + n2


def subtract(n1, n2):
    """subtract a number from another"""
    return n1 - n2


def multiply(n1, n2):
    """multiply 2 numbers"""
    return n1 * n2


def divide(n1, n2):
    """divide a number by another"""
    return n1 / n2


def main():
    """ "implement the calculator project from Day 10 L076"""
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    while True:
        print("\n" * 10)
        print(LOGO)
        ans = input("Enter the first number (q to exit): ").lower()
        if ans == "q":
            break
        n1 = float(ans)
        done = False
        while not done:
            for symbol in operations:
                print(symbol)
            operator = input("pick an operator: ")
            n2 = float(input("Enter the second number: "))
            ans = operations[operator](n1, n2)
            print(f"{n1} {operator} {n2} = {ans}")
            n1 = ans
            done = (
                input(
                    "Do you want to continue working with the previous result? (y/n): "
                ).lower()
                == "n"
            )


if __name__ == "__main__":
    main()
