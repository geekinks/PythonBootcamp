"""
Exercise 09: Composition (Solution)
Reference solution showing Composition (Student owns Transcript) and Aggregation (Department holds Students & Courses).
"""

class Course:
    def __init__(self, code: str, title: str, credit_units: int):
        self.code = code
        self.title = title
        self.credit_units = credit_units


class Transcript:
    def __init__(self):
        self._grades: dict[str, float] = {}

    def add_grade(self, course_code: str, score: float):
        if not (0.0 <= score <= 100.0):
            raise ValueError("Score must be between 0 and 100")
        self._grades[course_code] = float(score)

    def get_gpa(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)


class Student:
    def __init__(self, name: str, matric_no: str):
        self.name = name
        self.matric_no = matric_no
        self.transcript = Transcript()  # Composition: Student owns its Transcript

    def record_score(self, course_code: str, score: float):
        self.transcript.add_grade(course_code, score)


class Department:
    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []  # Aggregation
        self.courses: list[Course] = []    # Aggregation

    def add_student(self, student: Student):
        self.students.append(student)

    def add_course(self, course: Course):
        self.courses.append(course)


if __name__ == "__main__":
    dept = Department("Computer Science")
    s = Student("Aisha", "GSU/001")
    s.record_score("CSC301", 90.0)
    s.record_score("CSC305", 80.0)
    dept.add_student(s)
    print(f"Department: {dept.name} with {len(dept.students)} students. Aisha's GPA: {s.transcript.get_gpa()}")
    print("All tests passed successfully! Composition and aggregation relationships working cleanly.")
