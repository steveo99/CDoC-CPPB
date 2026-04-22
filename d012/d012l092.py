"""
100 Days of Code, Day 12, Lesson 92
Number Guessing Game
"""

import random
from d012.art import LOGO


def main():
    """
    Code for Day 12 Lesson 92
    Number Guessing game
    """
    while True:
        print("\n" * 20)
        print(LOGO)
        target = random.randint(1, 100)
        level = ""
        while level not in ["easy", "hard"]:
            level = input("enter a level (easy or hard): ").lower()
        tries = 10 if level == "easy" else 5
        success = False
        while tries > 0:
            guess = int(input("Guess a number between 1 and 100: "))
            tries -= 1
            if guess == target:
                success = True
                break
            message = "high" if guess > target else "low"
            tries_display = "tries" if tries > 1 else "try"
            print(f" too {message}. you have {tries} {tries_display} remaining")

        if success:
            print("Correct! You win.")
        else:
            print(f"Sorry, you lost. The number was {target}.")

        ans = input("Do you want to play again? (y/n): ").lower()
        if ans == "n":
            break


if __name__ == "__main__":
    main()
