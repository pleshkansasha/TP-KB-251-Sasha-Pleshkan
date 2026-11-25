def toPostfix(expression):
    stack = []
    output = []
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    expression = expression.replace(" ", "")
    number = ""
    for symbol in expression:
        if symbol.isdigit() or symbol == ".":
            number += symbol
            continue
        if number != "":
            output.append(number)
            number = ""
        if symbol == "(":
            stack.append(symbol)
        elif symbol == ")":
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        elif symbol in priority:
            while stack and stack[-1] in priority:
                if priority[stack[-1]] < priority[symbol]:
                    break
                if symbol == "^" and stack[-1] == "^":
                    break
                output.append(stack.pop())
            stack.append(symbol)
    if number != "":
        output.append(number)
    while stack:
        output.append(stack.pop())
    return output
def calculate(postfix):
    stack = []
    for symbol in postfix:
        if symbol not in ["+", "-", "*", "/", "^"]:
            stack.append(float(symbol))
        else:
            b = stack.pop()
            a = stack.pop()
            if symbol == "+":
                stack.append(a + b)
            elif symbol == "-":
                stack.append(a - b)
            elif symbol == "*":
                stack.append(a * b)
            elif symbol == "/":
                stack.append(a / b)
            elif symbol == "^":
                stack.append(a ** b)
    return stack.pop()
def main():
    expression = input("Enter expression: ")
    postfix = toPostfix(expression)
    print("Postfix:", " ".join(postfix))
    print("Result:", calculate(postfix))
if __name__ == "__main__":
    main()