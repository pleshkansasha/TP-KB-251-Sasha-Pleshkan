from sys import argv
from Student import Student
from StudentList import StudentList
from Utils import Utils
def main():
    studentList = StudentList()
    utils = Utils()
    file_name = argv[1]
    utils.loadFromFile(file_name, studentList)
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
                student = Student(name, phone, age, group)
                studentList.addNewElement(student)
                studentList.printAllList()
            case "U" | "u":
                name = input("Enter student name to update: ")
                newName = input("Enter new name: ")
                newPhone = input("Enter new phone: ")
                newAge = input("Enter new age: ")
                newGroup = input("Enter new group: ")
                student = Student(newName, newPhone, newAge, newGroup)
                studentList.updateElement(name, student)
                studentList.printAllList()
            case "D" | "d":
                name = input("Enter student name to delete: ")
                studentList.deleteElement(name)
                studentList.printAllList()
            case "P" | "p":
                studentList.printAllList()
            case "X" | "x":
                utils.saveToFile(file_name, studentList)
                print("Exit")
                break
            case _:
                print("Wrong choice")
if __name__ == "__main__":
    main()