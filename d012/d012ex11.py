"""
100 Days of Code, Day 12, Excercise 11
Prime Number Checker
"""

import math


def is_prime(num):
    """
    Check if num is prime, return True or False
    """
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    max_divisor = int(math.sqrt(num)) + 0.01
    divisor = 3
    while divisor <= max_divisor:
        if num % divisor == 0:
            return False
        divisor += 2
    return True


def main():
    """
    Code for Day 12 Exercise 11
    Prime Number Checker
    """
    while True:
        ans = input("Enter a number (q to exit): ")
        if ans == "q":
            return
        n = int(ans)
        print(f"{n} is {'prime' if is_prime(n) else 'not prime'}.")


if __name__ == "__main__":
    main()
