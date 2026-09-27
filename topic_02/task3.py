def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")
match operation:
    case "+":
        print(add(a, b))
    case "-":
        print(subtract(a, b))
    case "*":
        print(multiply(a, b))
    case "/":
        if b != 0:
            print(divide(a, b))
        else:
            print("На нуль ділити не можна")
    case _:
        print("Невідома операція")