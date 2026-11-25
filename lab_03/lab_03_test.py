from Student import Student
from StudentList import StudentList
from Utils import Utils
def test_add():
    students = StudentList()
    students.addNewElement(Student("Bob", "0631234567", "18", "KB-251"))
    assert len(students.students) == 1
    assert students.students[0].name == "Bob"
def test_delete():
    students = StudentList()
    students.addNewElement(Student("Bob", "0631234567", "18", "KB-251"))
    students.deleteElement("Bob")
    assert len(students.students) == 0
def test_update():
    students = StudentList()
    students.addNewElement(Student("Bob", "0631234567", "18", "KB-251"))
    students.updateElement("Bob", Student("Vasya", "0631234567", "19", "KB-251"))
    assert students.students[0].name == "Vasya"
    assert students.students[0].age == "19"
def test_load(tmp_path):
    students = StudentList()
    utils = Utils()
    file_name = tmp_path / "test.csv"
    file_name.write_text(
        "Name,Phone,Age,Group\nBob,0631234567,18,KB-251\n"
    )
    utils.loadFromFile(file_name, students)
    assert len(students.students) == 1
    assert students.students[0].name == "Bob"
def test_save(tmp_path):
    students = StudentList()
    utils = Utils()
    students.addNewElement(Student("Bob", "0631234567", "18", "KB-251"))
    file_name = tmp_path / "test.csv"
    utils.saveToFile(file_name, students)
    assert file_name.exists()
    assert "Bob,0631234567,18,KB-251" in file_name.read_text()