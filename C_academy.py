# C_academy.py
from A_models import Student, Course
from B_enrollment import Enrollment

class Academy:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student: Student):
        if any(s.id == student.id for s in self.students):
            raise ValueError("Studenti me këtë ID ekziston.")
        self.students.append(student)

    def add_course(self, course: Course):
        if any(c.code == course.code for c in self.courses):
            raise ValueError("Kursi me këtë kod ekziston.")
        self.courses.append(course)

    def find_student(self, student_id: int):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def find_course(self, course_code: str):
        for c in self.courses:
            if c.code == course_code:
                return c
        return None

    def enroll(self, student_id: int, course_code: str, paid: float):
        student = self.find_student(student_id)
        course = self.find_course(course_code)
        if not student or not course:
            raise ValueError("Studenti ose kursi nuk u gjet.")
        enrollment = Enrollment(student, course, paid)
        self.enrollments.append(enrollment)
        return enrollment

    def total_revenue(self):
        return sum(e.paid for e in self.enrollments)

    def due_by_course(self, code: str):
        return sum(e.remaining() for e in self.enrollments if e.course.code == code)

    def enroll_count_by_city(self, city: str):
        return sum(1 for e in self.enrollments if e.student.city == city)

    def report_course(self, code: str) -> str:
        total_paid = sum(e.paid for e in self.enrollments if e.course.code == code)
        total_due = sum(e.remaining() for e in self.enrollments if e.course.code == code)
        count = sum(1 for e in self.enrollments if e.course.code == code)
        return (f"Kursi {code} | Regjistrime: {count} | Të ardhura: {total_paid:.2f} EUR | "
                f"Mungesa: {total_due:.2f} EUR")

    def report_city(self, city: str) -> str:
        total_paid = sum(e.paid for e in self.enrollments if e.student.city == city)
        count = sum(1 for e in self.enrollments if e.student.city == city)
        return f"Qyteti {city} | Regjistrime: {count} | Të ardhura: {total_paid:.2f} EUR"
