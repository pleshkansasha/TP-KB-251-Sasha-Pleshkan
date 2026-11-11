class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
students = [
    Student("Саша", 18),
    Student("Андрій", 20),
    Student("Олена", 19)
]
for student in sorted(students, key=lambda x: x.age):
    print(student)
