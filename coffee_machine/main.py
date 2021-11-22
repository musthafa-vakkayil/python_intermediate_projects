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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 2.Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3.Print report.
# TODO: 4.Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.


def update(value,cash):
    for i in MENU[value]['ingredients']:
        resources[i] -= MENU[value]['ingredients'][i]
    resources["Profit"] = round(cash, 2)
    print(f"Here is Your {value} ☕ Enjoy!")
    on()


def check(value):
    for i in MENU[value]['ingredients']:
        if MENU[value]['ingredients'][i] > resources[i]:
            return False
    return True


def coin(value):
    print("Please Insert Coins")
    quarters = int(input("How Many Quarters : "))
    dimes = int(input("How Many Dimes : "))
    nickles = int(input("How Many Nickles : "))
    pennies = int(input("How Many pennies : "))

    money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    item_cost = MENU[value]['cost']

    if money < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        on()
    elif money == item_cost:
        update(value,money)
    else:
        money = money - item_cost
        print(f"Here is {round(money,2)} dollars in change.")
        update(value,money)


def on():
    operation = input("What would you like? (espresso/latte/cappuccino): ")

    if operation == "off":
        return
    elif operation == "report":
        for item in resources:
            print(f"{item} : {resources[item]}")
        on()
    elif check(operation):
        coin(operation)
    else:
        for i in MENU[operation]['ingredients']:
            if MENU[operation]['ingredients'][i] > resources[i]:
                print(f"There is No Sufficient {i}")
        on()


on()









