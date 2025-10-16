# B_enrollment.py
from A_models import Student, Course

class Enrollment:
    def __init__(self, student: Student, course: Course, paid: float):
        if paid < 0 or paid > course.price:
            raise ValueError("Pagesa duhet të jetë midis 0 dhe çmimit të kursit.")
        self.student = student
        self.course = course
        self.paid = paid

    def remaining(self) -> float:
        return self.course.price - self.paid

    def __str__(self):
        return (f"Enroll[Student {self.student.id} -> {self.course.code}] "
                f"Paid: {self.paid:.2f} EUR | Remain: {self.remaining():.2f} EUR")
