def diskr(a, b, c):
    D = b * b - 4 * a * c
    return D

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))
D = diskr(a, b, c)

print("D = ", D)