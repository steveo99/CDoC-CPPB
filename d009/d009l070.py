from D009.art import logo


def main():

    def find_highest_bidder(bidding_dictionary):
        winner = ""
        highest_bid = 0
        for bidder, bid in bidding_dictionary.items():
            if bid > highest_bid:
                highest_bid = bid
                winner = bidder
        return winner, highest_bid

    # TODO-1: Ask the user for input
    bids = {}
    while True:
        print("\n" * 50)
        print(logo)
        name = input("What is your name? ")
        price = int(input("What is your bid? "))

        # TODO-2: Save data into dictionary {name: price}
        bids[name] = price

        # TODO-3: Whether if new bids need to be added
        ans = input("Are there any other bids? (y/n) ")
        if ans == "n":
            break

    # TODO-4: Compare bids in dictionary
    winner, highest_bid = find_highest_bidder(bids)
    print(f"the winner is {winner} with a bid of ${highest_bid}")


if __name__ == "__main__":
    main()
