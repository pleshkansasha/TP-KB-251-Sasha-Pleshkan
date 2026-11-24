from lab_02 import students, addNewElement, deleteElement
from lab_02 import updateElement, loadFromFile, saveToFile
def test_add():
    students.clear()
    addNewElement("Bob", "0631234567", "18", "KB-251")
    assert len(students) == 1
    assert students[0]["name"] == "Bob"
def test_delete():
    students.clear()
    addNewElement("Bob", "0631234567", "18", "KB-251")
    deleteElement("Bob")
    assert len(students) == 0
def test_update():
    students.clear()
    addNewElement("Bob", "0631234567", "18", "KB-251")
    updateElement("Bob", "Vasya", "0631234567", "19", "KB-251")
    assert students[0]["name"] == "Vasya"
    assert students[0]["age"] == "19"
def test_load(tmp_path):
    file_name = tmp_path / "test.csv"
    file_name.write_text(
        "Name,Phone,Age,Group\nBob,0631234567,18,KB-251\n"
    )
    loadFromFile(file_name)
    assert len(students) == 1
    assert students[0]["name"] == "Bob"
def test_save(tmp_path):
    students.clear()
    addNewElement("Bob", "0631234567", "18", "KB-251")
    file_name = tmp_path / "test.csv"
    saveToFile(file_name)
    assert file_name.exists()
    assert "Bob,0631234567,18,KB-251" in file_name.read_text()