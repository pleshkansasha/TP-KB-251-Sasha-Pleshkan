from calculator import Calculator
calc = Calculator()
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")
if operation == "+":
    print(calc.add(a, b))
elif operation == "-":
    print(calc.subtract(a, b))
elif operation == "*":
    print(calc.multiply(a, b))
elif operation == "/":
    if b != 0:
        print(calc.divide(a, b))
    else:
        print("На нуль ділити не можна")
else:
    print("Невідома операція")