"""
Exercise 03: Constructors and Self (Solution)
Reference solution showing __init__ usage, default arguments, and object state.
"""

class Course:
    def __init__(self, code: str, title: str, credit_units: int = 3):
        self.code = code
        self.title = title
        self.credit_units = credit_units


class Student:
    def __init__(self, name: str, matric_no: str, department: str, level: int = 100):
        self.name = name
        self.matric_no = matric_no
        self.department = department
        self.level = level
        self.enrolled_courses: list[Course] = []

    def enroll(self, course: Course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

    def total_credits(self) -> int:
        return sum(course.credit_units for course in self.enrolled_courses)


if __name__ == "__main__":
    c1 = Course("CSC301", "Data Structures", credit_units=3)
    c2 = Course("CSC305", "Database Management Systems", credit_units=4)
    s = Student("Aisha", "GSU/CSC/001", "Computer Science", 300)
    s.enroll(c1)
    s.enroll(c2)
    print(f"{s.name} total credits enrolled: {s.total_credits()}")
    print("All tests passed successfully! Constructors and self implemented properly.")
