"""
100 Days of Code, Day 16b, Lesson 113
OOP Coffee Machine
"""

from d016b.menu import Menu, MenuItem
from d016b.coffee_maker import CoffeeMaker
from d016b.money_machine import MoneyMachine


def main():
    """
    Code for Day 16b Lesson 113
    OOP Coffee Machine
    """

    menu = Menu()
    # menu_item = MenuItem()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    options_string = menu.get_items()
    options_string = options_string.rstrip("/")
    options_list = options_string.split("/")
    options_list.append("report")
    options_list.append("off")
    print(options_list)

    is_on = True
    while is_on:
        # prompt user
        choice = ""
        while choice not in options_list:
            options_string = menu.get_items()
            choice = input(f"What would you like ({options_string}): ").lower()

        if choice == "off":
            is_on = False
            continue

        if choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink = menu.find_drink(choice)
        if not drink:
            print(f"{choice} not found.")
            continue
        # check that resources are sufficient
        if not coffee_maker.is_resource_sufficient(drink):
            continue

        # take payment
        if not money_machine.make_payment(drink.cost):
            continue

        # make coffee
        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
