import csv
from sys import argv
students = []
def loadFromFile(file_name):
    students.clear()
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row["Name"],
                "phone": row["Phone"],
                "age": row["Age"],
                "group": row["Group"]
            })
    students.sort(key=lambda x: x["name"])
def saveToFile(file_name):
    with open(file_name, "w", newline="") as file:
        fieldnames = ["Name", "Phone", "Age", "Group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow({
                "Name": student["name"],
                "Phone": student["phone"],
                "Age": student["age"],
                "Group": student["group"]
            })
def printAllList():
    for student in students:
        print("Name:", student["name"],
              "Phone:", student["phone"],
              "Age:", student["age"],
              "Group:", student["group"])
def addNewElement(name, phone, age, group):
    newItem = {
        "name": name,
        "phone": phone,
        "age": age,
        "group": group
    }
    insertPosition = 0
    for student in students:
        if name > student["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New student has been added")
def deleteElement(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student has been deleted")
            return
    print("Student was not found")
def updateElement(name, newName, newPhone, newAge, newGroup):
    for student in students:
        if student["name"] == name:
            student["name"] = newName
            student["phone"] = newPhone
            student["age"] = newAge
            student["group"] = newGroup
            students.sort(key=lambda x: x["name"])
            print("Student information has been updated")
            return
    print("Student was not found")
def main():
    file_name = argv[1]
    loadFromFile(file_name)
    while True:
        choice = input(
            "\nChoose action [C create, U update, "
            "D delete, P print, X exit]: "
        )
        match choice:
            case "C" | "c":
                name = input("Enter student name: ")
                phone = input("Enter student phone: ")
                age = input("Enter student age: ")
                group = input("Enter student group: ")
                addNewElement(name, phone, age, group)
                printAllList()
            case "U" | "u":
                name = input("Enter student name to update: ")
                newName = input("Enter new name: ")
                newPhone = input("Enter new phone: ")
                newAge = input("Enter new age: ")
                newGroup = input("Enter new group: ")
                updateElement(name, newName, newPhone, newAge, newGroup)
                printAllList()
            case "D" | "d":
                name = input("Enter student name to delete: ")
                deleteElement(name)
                printAllList()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                saveToFile(file_name)
                print("Exit")
                break
            case _:
                print("Wrong choice")
if __name__ == "__main__":
    main()