# D_report_demo.py
from A_models import Student, Course
from C_academy import Academy

academy = Academy()

# Studentët
academy.add_student(Student(1, "Shqipe Kola", "Tiranë", 17))
academy.add_student(Student(2, "Ardit Hysa", "Durrës", 19))
academy.add_student(Student(3, "Elira Dema", "Tiranë", 18))
academy.add_student(Student(4, "Besnik Lika", "Fier", 20))

# Kurset
academy.add_course(Course("PY", "Python", 120.0))
academy.add_course(Course("EX", "Excel", 80.0))

# Regjistrimet
academy.enroll(1, "PY", 80.0)
academy.enroll(2, "EX", 80.0)
academy.enroll(3, "PY", 100.0)
academy.enroll(4, "PY", 100.0)
academy.enroll(3, "EX", 80.0)

# Raporte
print(academy.report_course("PY"))
print(academy.report_course("EX"))
print(academy.report_city("Tiranë"))
print(academy.report_city("Durrës"))
