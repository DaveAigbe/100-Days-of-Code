from resource_data import MENU, resources


def view_report():
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")  # Print out the individual resources from the resources tab, this will be updated each time user enters


def checking_resources(choice):
    """Check to see if there are enough resources inside the machine to make the users drink"""
    for resource in MENU[choice]['ingredients']:  # for each ingredient in the specified choice
        if MENU[choice]['ingredients'][resource] <= resources[resource]:  # if the ingredient is less than or equal to the amount in the machine
            return True  # The drink can be made
        else:
            return False  # Otherwise, the drink cannot be made


def using_resources(choice):
    """Subtract the resources from the machine resources based off of users drink"""
    for resource in MENU[choice]['ingredients']:  # for each ingredient in the specified choice
        resources[resource] -= MENU[choice]['ingredients'][resource]  # new resources in the machine is equal to current resources in the machine minus the resources needed by the drink


def calculate_money():
    """Calculate the users total payment from the coins given."""
    print("Please insert your coins now.")
    quarters = float(input("How many quarters? (25¢): ")) * .25  # Everything below shows however many of each coin they will use, multiplied by the coin value
    dimes = float(input("How many dimes? (10¢): ")) * .10
    nickles = float(input("How many nickles? (5¢): ")) * .05
    pennies = float(input("How many pennies? (1¢): ")) * .01

    total_cash = quarters + dimes + nickles + pennies  # Showing users total cash to pay for drink
    return total_cash


def money_and_resources(choice):
    """Does all the work for the program, dictates what will happen each time user input is changed"""
    if choice == 'report':  # if user enters report, display resources left and money collected
        view_report()
    elif choice == 'off':  # to turn the machine off
        exit()
    else:
        if checking_resources(choice):  # if resources are still available to make the drink
            print(f"Your total will be ${MENU[choice]['cost']}")  # print the total cost of the drink from the 'cost' key
            total_cash = calculate_money()
            change = round((total_cash - MENU[choice]['cost']), 2)

            if total_cash == MENU[choice]['cost']:  # If the cash given matches the exact amount of the drink
                print(f"Exact amount given. No change to dispense.")
                print(f"Here is your {choice} ☕. Enjoy! ")
                resources['money'] += total_cash  # Add the money to the dictionary holding the resources (All the cash given, except the extra if applicable)
                using_resources(choice)  # deduct the resources, based off of user choice, from the current resources in the machine
            elif total_cash > MENU[choice]['cost']:  # If the cash given is over the amount of the drink
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy! ")
                resources['money'] += (total_cash - change)
                using_resources(choice)
            elif total_cash < MENU[choice]['cost']:  # If the cash given is under the amount of the drink
                print("Sorry that's not enough money. Money refunded.")
        else:  # If their one or more resources is missing
            if resources['water'] == 0 or resources['milk'] == 0 or resources['coffee'] == 0: # If any of the resources hit zero (Water would prob be first), then the machine will not be able to make anymore drinks
                print("\nNo drinks can be made at this time for maintenance purposes, we apologize for the inconvenience.")
                print("Have a great day! Thank you!😀")
                exit()
            else:
                empty = ''
                for resource in MENU[choice]['ingredients']:
                    if resources[resource] - MENU[choice]['ingredients'][resource] <= 0:
                        empty = resource
                print(f"Sorry there is not enough {empty}.")

