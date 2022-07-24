from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

vending_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    user_choice = input(f"Please enter your drink of choice ({vending_menu.get_items()}): ")
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'off':
        print("Shutting Down...")
        exit()
    else:
        drink = vending_menu.find_drink(user_choice)
        if drink:  # If drink did not return None
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                continue
        else:
            continue

