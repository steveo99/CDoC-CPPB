"""100 Days of Code, Day 11, Lesson nnn - Blackjack Program"""

import random
from d011.art import LOGO

CARD_LIST = [
    11,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
]


def draw_card():
    """return a random card"""
    return CARD_LIST[random.randint(0, len(CARD_LIST) - 1)]


def show_hand(cards):
    """show the cards in a hand"""
    return ", ".join(str(card) for card in cards)


def show_first_card(cards):
    """show the first card of a hand"""
    cards = str(cards[0])
    return cards


def get_hand_total(cards):
    """calculate the total of a hand"""
    while True:
        hand_total = sum(cards)
        if hand_total > 21 and 11 in cards:
            cards[cards.index(11)] = 1
        else:
            break
    return hand_total


def determine_winner(player, dealer):
    """determine the winning hand, or Draw if a tie"""
    p = get_hand_total(player)
    d = get_hand_total(dealer)

    if p > 21:
        result = "Dealer"
    elif d > 21:
        result = "Player"
    elif p == d:
        result = "Draw"
    elif p > d:
        result = "Player"
    else:
        result = "Dealer"
    return result


def play_game():
    """play a hand of blackjack, return the winner: Player or Dealer, or Draw if a tie"""
    player = []
    dealer = []
    player.append(draw_card())
    dealer.append(draw_card())
    player.append(draw_card())
    dealer.append(draw_card())

    print("\n" * 10)
    print(LOGO)
    while True:
        print(f"Player: {show_hand(player)} = {get_hand_total(player)}")
        print(f"Dealer: {show_first_card(dealer)}")
        ans = input("Do you want another card? (y/n): ").lower()
        if ans == "y":
            player.append(draw_card())
            print(f"Player draws {player[-1]}")
            if get_hand_total(player) > 21:
                break
        else:
            break

    print()
    while True:
        print(f"Dealer: {show_hand(dealer)} = {get_hand_total(dealer)}")
        d = get_hand_total(dealer)
        if d < 17:
            dealer.append(draw_card())
            print(f"Dealer draws {dealer[-1]}")
        else:
            break

    print()
    print(f"Player: {show_hand(player)} = {get_hand_total(player)}")
    print(f"Dealer: {show_hand(dealer)} = {get_hand_total(dealer)}")
    winner = determine_winner(player, dealer)
    if winner == "Draw":
        print("It's a Draw")
    else:
        print(f"{winner} wins.")
    return winner


def main():
    """Code for Day 11 Lesson 79 - Blackjack Project"""
    games = 0
    player = 0
    dealer = 0
    draws = 0
    while True:
        winner = play_game()
        games += 1
        if winner == "Player":
            player += 1
        elif winner == "Dealer":
            dealer += 1
        else:
            draws += 1

        print(
            f"games: {games}, player won {player}, dealer won {dealer}, draws {draws}"
        )
        ans = input("Do you want to play again? (y/n): ")
        if ans == "n":
            break


if __name__ == "__main__":
    main()
