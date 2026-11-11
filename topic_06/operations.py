def getnumber():
    while True:
        try:
            return float(input("Введіть число: "))
        except ValueError:
            print("Неправильне число")
def getoperation():
    return input("Введіть операцію (+, -, *, /) або exit: ")