def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
while True:
    operation = input("Операція (+, -, *, /), 0 - вихід: ")
    if operation == "0":
        exit()
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))
    if operation == "+":
        print(add(a, b))
    elif operation == "-":
        print(subtract(a, b))
    elif operation == "*":
        print(multiply(a, b))
    elif operation == "/":
        if b != 0:
            print(divide(a, b))
        else:
            print("На нуль ділити не можна")
    else:
        print("Невідома операція")