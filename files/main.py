import unittest


class TestFile(unittest.TestCase):
    def test_add_last_student(self):
        new_student = "Lucas Tester"
        older_last_id, older_name = get_last_student()
        add_student(new_student)
        id_str_new, new_name = get_last_student()
        self.assertEqual(id_str_new, str(int(older_last_id) + 1), "new id should be older last id + 1")
        self.assertEqual(new_name, new_student, "new name should be " + new_student)


def get_mark(id_student: int) -> int or None:
    califications_file = open('califications.dat')
    line_calif = califications_file.readline()
    while line_calif != "":
        calification = line_calif.strip().split(';')
        if int(calification[0]) == id_student:
            suma = 0
            for i in range(1, len(calification)):
                suma += int(calification[i])
            califications_file.close()
            return round(suma / (len(calification) - 1))
        line_calif = califications_file.readline()
    califications_file.close()
    return None


def get_last_student() -> [int, str]:
    names_file = open('students.dat', 'r')
    last = ""
    for line in names_file:
        last = line
    names_file.close()
    if last == "":
        return [0, ""]
    return last.split(';')


def add_student(name: str):
    students_file = open('students.dat', 'a')
    id_str, last_student_name = get_last_student()
    id_str = str(int(id_str) + 1)
    students_file.write("\n" + id_str + ";" + name)
    students_file.close()


def get_marks_average() -> dict:
    students_file = open('students.dat', 'r')
    califications = {}
    for line in students_file:
        id_user, name = line.strip().split(';')
        califications[name] = get_mark(int(id_user))
    students_file.close()
    return califications


def add_mark(notas: [int]):
    marks_file = open('califications.dat', 'a')
    print("Registrar nuevo alumno con sus notas: ")
    id_st, name = get_last_student()
    id_st = str(int(id_st) + 1)
    for nota in notas:
        id_st += ";" + str(round(nota))
    marks_file.write("\n" + id_st)
    marks_file.close()


def modify_calification():
    pass
