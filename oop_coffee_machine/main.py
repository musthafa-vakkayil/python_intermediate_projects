from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


m = Menu()
c = CoffeeMaker()
a = MoneyMachine()

def coffee_machine():
    while(True):
        print(f"What Would You Like {m.get_items()}:")
        response = input()

        if(response == "off"):
            exit()

        if(response == "report"):
            c.report()
            a.report()

        elif(m.find_drink(response)):
            drink = m.find_drink(response)
            if(c.is_resource_sufficient(drink)):
                if(a.make_payment(drink.cost)):
                    c.make_coffee(drink)

coffee_machine()