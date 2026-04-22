"""
100 Days of Code, Day 14, Lesson 102
Higher Lower Project
"""

import random
from d014.art import LOGO, VS
from d014.game_data import DATA


def print_higher_lower():
    """
    print the higher lower logo
    """
    print("\n" * 20)
    print(LOGO)


def get_choice_info(index):
    """
    getthe display string for the given index
    """
    d = DATA[index]
    return f"{d['name']}, {d['description']}, from {d['country']}."


def print_choice(prefix, index):
    """
    print the display string for the given index
    """
    print(f"{prefix}: {get_choice_info(index)}")


def play_game():
    """
    play the game
    """
    data_len = len(DATA)
    wins = 0
    game_over = False

    # get the first choice
    # put it in index_b, the loop will move it to index_a
    index_b = random.randint(0, data_len - 1)

    print_higher_lower()
    # print(f"{index_a=}")

    while not game_over:
        # make choice A be the previous choice B
        index_a = index_b
        # get a new choice_b index
        while index_b == index_a:
            index_b = random.randint(0, data_len - 1)

        print_choice("Compare A", index_a)
        print(VS)
        print_choice("Against B", index_b)

        # print question
        ans = ""
        while ans not in ["A", "B"]:
            ans = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_followers = DATA[index_a]["follower_count"]
        b_followers = DATA[index_b]["follower_count"]
        # print(f"{a_followers=}, {b_followers=}")

        correct_answer = "A" if a_followers > b_followers else "B"

        if ans == correct_answer:
            wins += 1
            print_higher_lower()
            print(f"You're right! Current score: {wins}.")
        else:
            game_over = True

    print_higher_lower()
    print(f"Sorry, that's wrong. Final score: {wins}")


def main():
    """
    100 Days of Code, Day 14, Lesson 102
    Higher Lower Project
    """
    while True:
        play_game()
        ans = ""
        while ans not in ["y", "n"]:
            ans = input("Do you want to play again? (y/n): ").lower()
        if ans == "n":
            break


if __name__ == "__main__":
    main()
