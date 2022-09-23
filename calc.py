def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def main():
    a = int(input("Please input a number:"))
    b = int(input("Please input a number:"))
    operation = input("choose choice of operation, +, -, *,/:")
    if operation == "+":
        print(f"The addition of numbers=", add(a, b))
    if operation == "-":
        print(f"The subtraction of numbers=", sub(a, b))
    if operation == "*":
        print(f"The multiplication of numbers=", mult(a, b))
    elif operation == "/":
        print(f"The division of numbers=", div(a, b))


main()