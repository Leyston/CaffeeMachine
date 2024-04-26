import data

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def chose_coins():
    total = 0
    print("Please insert coins.")
    for i in coins:
        value = float(input(f"How many {i}?: "))
        total += coins[i] * value
    return round(total, 2)


def transaction(choice, total):
    if total < data.MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - data.MENU[choice]["cost"]
        if change == 0:
            make_coffee(choice)
            data.resources["money"] += total
        else:
            print(f"Here is ${change} dollars in change")
            make_coffee(choice)
            data.resources["money"] += (total - change)


def make_coffee(choice):
    for i in data.MENU[choice]["ingredients"]:
        data.resources[i] -= data.MENU[choice]["ingredients"][i]
    print(f"Here is your {choice}")
