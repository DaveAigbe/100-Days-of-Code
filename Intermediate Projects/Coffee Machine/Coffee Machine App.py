from machine_functions import money_and_resources
from art import logo

print(logo,'\n')
print("Welcome to the coffee vending machine.\n")
running = True

while running:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ")
    money_and_resources(user_drink)

