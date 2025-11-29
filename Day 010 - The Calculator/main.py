import os
from art import logo

print(logo)
print("Welcome to the PyCalculator!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "Can't divide by zero."
    return num1 / num2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def calculator():
    should_accumulate = True
    number1 = float(input("What is the first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick up an operation: ")
        number2 = float(input("What is the next number: "))

        answer = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer:.2f}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice in ["yes", "y"]:
            number1 = answer
            continue
        else:
            should_accumulate = False
            clear_screen()
            calculator()

calculator()