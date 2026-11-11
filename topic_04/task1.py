def getNumber():
    while True:
        try:
            number = float(input("Введіть число: "))
            return number
        except ValueError:
            print("Неправильне число")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
while True:
    operation = input("Введіть операцію (+, -, *, /) або exit: ")
    if operation == "exit":
        break
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        a = getNumber()
        b = getNumber()
        if operation == "+":
            print(add(a, b))
        elif operation == "-":
            print(subtract(a, b))
        elif operation == "*":
            print(multiply(a, b))
        elif operation == "/":
            try:
                print(divide(a, b))
            except ZeroDivisionError:
                print("На нуль ділити не можна")
    else:
        print("Невідома операція")
        