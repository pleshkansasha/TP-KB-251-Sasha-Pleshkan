class StudentList:
    def __init__(self):
        self.students = []
    def printAllList(self):
        for student in self.students:
            print("Name:", student.name,
                  "Phone:", student.phone,
                  "Age:", student.age,
                  "Group:", student.group)
    def addNewElement(self, student):
        self.students.append(student)
        self.students.sort(key=lambda x: x.name)
    def deleteElement(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return
        print("Student not found")
    def updateElement(self, name, newStudent):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                self.addNewElement(newStudent)
                return
        print("Student not found")
        