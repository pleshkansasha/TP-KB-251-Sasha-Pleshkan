import random
user = input("Введіть stone, scissor або paper: ")
computer = random.choice(["stone", "scissor", "paper"])
print("Комп'ютер вибрав:", computer)
if user == computer:
    print("Нічия")
elif user == "stone" and computer == "scissor":
    print("Ви перемогли")
elif user == "scissor" and computer == "paper":
    print("Ви перемогли")
elif user == "paper" and computer == "stone":
    print("Ви перемогли")
else:
    print("Комп'ютер переміг")
    