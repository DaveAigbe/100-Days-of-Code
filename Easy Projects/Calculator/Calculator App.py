from Art import logo as logo
from operations import add as add, subtract as subtract , multiply as multiply, divide as divide

print(logo)


def calculator():
    first_num = float(input("Whats the first number?: "))
    stop_running = False
    while not stop_running:
        print("+\n-\n*\n/\n")
        operation = (input("Pick an operation: "))
        second_num = float(input("Whats the next number?: "))
        answer = 0
        if operation == '+':
            answer = add(first_num, second_num)
        elif operation == '-':
            answer = subtract(first_num, second_num)
        elif operation == '*':
            answer = multiply(first_num, second_num)
        elif operation == '/':
            answer = divide(first_num, second_num)
        else:
            print("Invalid Choice")

        print(f"{first_num} {operation} {second_num} = {answer} ")
        same_number = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'quit' to exit program:  ").lower()
        if same_number == 'y':
            first_num = answer
        elif same_number == 'n':
            calculator()  # recursion
        else:
            stop_running = True


calculator()













