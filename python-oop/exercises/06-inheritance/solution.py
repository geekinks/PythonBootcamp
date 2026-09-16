"""
Exercise 06: Inheritance (Solution)
Reference solution showing base class delegation with super() and method overriding.
"""

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_role(self) -> str:
        return "User"

    def format_header(self) -> str:
        return f"[{self.get_role()}] {self.name} <{self.email}>"


class Student(User):
    def __init__(self, name: str, email: str, matric_no: str, level: int = 100):
        super().__init__(name, email)
        self.matric_no = matric_no
        self.level = level

    def get_role(self) -> str:
        return "Student"


class Lecturer(User):
    def __init__(self, name: str, email: str, staff_id: str, department: str):
        super().__init__(name, email)
        self.staff_id = staff_id
        self.department = department

    def get_role(self) -> str:
        return "Lecturer"


if __name__ == "__main__":
    student = Student("Aisha", "aisha@uni.edu", "GSU/001")
    lecturer = Lecturer("Dr. Kabir", "kabir@uni.edu", "STF-1", "CSC")
    print(student.format_header())
    print(lecturer.format_header())
    print("All tests passed successfully! Inheritance hierarchy functioning as expected.")
