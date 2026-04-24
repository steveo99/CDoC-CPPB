"""
100 Days of Code, Day 15, Lesson 105
Coffee Machine Project
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0


# Print a report of all the coffee machine resources
def print_report():
    """
    print a report of resources remaining
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


# Check resources sufficient to make drink order
def resources_required(order):
    """
    return the ingredients required and the cost for the drink in order
    """
    water_needed = MENU[order]["ingredients"].get("water", 0)
    milk_needed = MENU[order]["ingredients"].get("milk", 0)
    coffee_needed = MENU[order]["ingredients"].get("coffee", 0)
    cost = MENU[order]["cost"]
    return water_needed, milk_needed, coffee_needed, cost


def check_resources(order):
    """
    check if there are enough resources to prepare the drink in order
    """
    enough_resources = True
    water_needed, milk_needed, coffee_needed, _ = resources_required(order)
    if resources["water"] < water_needed:
        enough_resources = False
        print("Sorry, there is not enough water.")
    if resources["milk"] < milk_needed:
        enough_resources = False
        print("Sorry, there is not enough milk.")
    if resources["coffee"] < coffee_needed:
        enough_resources = False
        print("Sorry, there is not enough coffee.")
    return enough_resources


# Process Coins
def process_coins(order):
    """
    prompt for the number of coins entered
    determine if enough was entered to purchase the order
    return change if extra was entered.
    """
    cost = MENU[order]["cost"]
    quarters = int(f"0{input("Quarters: ")}")
    dimes = int(f"0{input("Dimes: ")}")
    nickles = int(f"0{input("Nickles: ")}")
    pennies = int(f"0{input("Pennies: ")}")
    coin_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if coin_value < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    if coin_value > cost:
        print(f"Here's ${coin_value - cost:.2f} in change.")
    return True


# Make coffee
def make_coffee(order):
    """
    prepare the drink ordered
    reduce resources by the amounts used to make the drink
    increment money by the cost
    """
    global money  # pylint: disable=global-statement
    water_needed, milk_needed, coffee_needed, cost = resources_required(order)
    # deduct the resources used
    resources["water"] -= water_needed
    resources["milk"] -= milk_needed
    resources["coffee"] -= coffee_needed
    # add the cost to money
    money += cost
    print(f"Here is your {order}. Enjoy!")


def main():
    """
    Code for Day 15 Lesson 105
    Coffee Machine Project
    """
    is_on = True
    while is_on:
        # Prompt the user
        print("\n")
        order = ""
        while order not in ["espresso", "latte", "cappuccino", "report", "off"]:
            order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            print_report()
            continue
        if order == "off":
            # Turn off by entering off to the prompt
            print("Turning off the coffee machine.")
            is_on = False
            continue

        # check resources
        if not check_resources(order):
            continue

        # process coins
        if not process_coins(order):
            continue

        # make coffee
        make_coffee(order)


if __name__ == "__main__":
    main()
