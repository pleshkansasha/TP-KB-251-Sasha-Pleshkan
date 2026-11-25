import csv
from Student import Student
class Utils:
    def loadFromFile(self, file_name, studentList):
        studentList.students.clear()
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["Name"], row["Phone"],
                                  row["Age"], row["Group"])
                studentList.addNewElement(student)
    def saveToFile(self, file_name, studentList):
        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file,
                fieldnames=["Name", "Phone", "Age", "Group"])
            writer.writeheader()
            for student in studentList.students:
                writer.writerow({
                    "Name": student.name,
                    "Phone": student.phone,
                    "Age": student.age,
                    "Group": student.group
                })