class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student name is {self.name}, age is {self.age}"
student = Student("Саша", 18)
print(student)