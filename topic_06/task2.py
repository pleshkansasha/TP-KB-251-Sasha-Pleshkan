students = [
    {"name": "Олена", "mark": 80},
    {"name": "Андрій", "mark": 50},
    {"name": "Марія", "mark": 60}
]
print("Sort by name:")
for student in sorted(students, key=lambda x: x["name"]):
    print(student)
print("Sort by mark:")
for student in sorted(students, key=lambda x: x["mark"]):
    print(student)