import data


def report():
    print(f"Water: {data.resources["water"]}ml")
    print(f"Milk: {data.resources["milk"]}ml")
    print(f"Coffee: {data.resources["coffee"]}g")
    print(f"Money: ${data.resources["money"]}")


def are_the_resources_sufficient(chose):
    print(chose)

    for i in data.MENU[chose]["ingredients"]:
        if data.MENU[chose]["ingredients"][i] > data.resources[i]:
            result = f"Sorry there is not enough {i}."
            return False, result
    return True, "nothing"
