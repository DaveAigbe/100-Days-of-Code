from operations import operations as operations
from Art import logo as logo

print(logo)


def calculator():
    should_continue = True
    first_num = float(input("Whats the first number?: "))
    while should_continue:

        for symbol in operations:
            print(symbol)
        operation = (input("Pick an operation from the options above: "))

        second_num = float(input("Whats the next number?: "))

        answer = (operations[operation](first_num, second_num))
        print(f"{first_num} {operation} {second_num} = {answer}")

        same_number = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'quit' to exit program:  ").lower()
        if same_number == 'y':
            first_num = answer
        elif same_number == 'n':
            calculator()
        elif same_number == "quit":
            break


calculator()