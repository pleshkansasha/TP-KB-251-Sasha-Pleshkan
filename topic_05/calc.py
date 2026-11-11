from functions import add, subtract, multiply, divide
from operations import getnumber, getoperation

while True:
    operation = getoperation()
    if operation == "exit":
        break
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        a = getnumber()
        b = getnumber()
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