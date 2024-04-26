import data
import resources
import transaction


def coffee_machine():
    state = "on"
    while state == "on":
        chose = input("What yould you like? (espresso/latte/cappuccino): ").lower()

        if chose == "off":
            state = "off"
        elif chose == "report":
            resources.report()
        else:
            value, text = resources.are_the_resources_sufficient(chose)
            if not value:
                print(text)
            else:
                coins = transaction.chose_coins()
                print(coins)
                transaction.transaction(chose, coins)
