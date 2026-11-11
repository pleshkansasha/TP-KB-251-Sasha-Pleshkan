from functions import add, subtract, multiply, divide
from operations import getnumber, getoperation
import logging

logging.basicConfig(filename="calc.log", level=logging.INFO)

while True:
    operation = getoperation()
    if operation == "exit":
        logging.info("Calculator exited")
        break
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        a = getnumber()
        b = getnumber()
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            try:
                result = divide(a, b)
            except ZeroDivisionError:
                print("На нуль ділити не можна")
                logging.info(f"{a} / {b} = division by zero")
                continue
        print(result)
        logging.info(f"{a} {operation} {b} = {result}")
    else:
        print("Невідома операція")
        logging.info(f"Unknown operation: {operation}")