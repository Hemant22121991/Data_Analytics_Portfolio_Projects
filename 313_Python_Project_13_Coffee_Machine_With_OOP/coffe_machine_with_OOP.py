from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if not drink:
            is_on = False
        elif coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
    