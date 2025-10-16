# A_models.py

class Student:
    def __init__(self, id: int, full_name: str, city: str, age: int):
        if not full_name.strip():
            raise ValueError("Emri nuk mund të jetë bosh.")
        if age < 15:
            raise ValueError("Mosha duhet të jetë ≥ 15.")
        self.id = id
        self.full_name = full_name
        self.city = city
        self.age = age

    def __str__(self):
        return f"Student[{self.id}] {self.full_name}, {self.city} ({self.age} vjeç)"


class Course:
    def __init__(self, code: str, title: str, price: float):
        if len(code) < 2:
            raise ValueError("Kodi duhet të ketë ≥ 2 karaktere.")
        if price < 0:
            raise ValueError("Çmimi duhet të jetë ≥ 0.")
        self.code = code
        self.title = title
        self.price = price

    def __str__(self):
        return f"Course[{self.code}] {self.title} — {self.price:.2f} EUR"
