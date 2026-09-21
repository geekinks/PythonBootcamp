"""
Exercise 09: Composition (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class Course:
    def __init__(self, code: str, title: str, credit_units: int):
        self.code = code
        self.title = title
        self.credit_units = credit_units


class Transcript:
    def __init__(self):
        # TODO 1: Initialize protected dict _grades = {}
        pass

    def add_grade(self, course_code: str, score: float):
        # TODO 2: Validate 0 <= score <= 100, then store in _grades
        pass

    def get_gpa(self) -> float:
        # TODO 3: Return average of scores or 0.0 if empty
        pass


class Student:
    def __init__(self, name: str, matric_no: str):
        self.name = name
        self.matric_no = matric_no
        # TODO 4: Initialize self.transcript as a new Transcript instance (Composition)
        pass

    def record_score(self, course_code: str, score: float):
        # TODO 5: Delegate adding grade to self.transcript
        pass


class Department:
    def __init__(self, name: str):
        self.name = name
        # TODO 6: Initialize empty lists self.students and self.courses (Aggregation)
        pass

    def add_student(self, student: Student):
        # TODO 7: Append student
        pass

    def add_course(self, course: Course):
        # TODO 8: Append course
        pass


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    dept = Department("Computer Science")
    c1 = Course("CSC301", "Python OOP", 3)
    c2 = Course("CSC305", "Database Systems", 3)

    s1 = Student("Aisha Muhammad", "GSU/CSC/001")
    s1.record_score("CSC301", 90.0)
    s1.record_score("CSC305", 80.0)

    assert s1.transcript.get_gpa() == 85.0, f"Expected 85.0 GPA, got {s1.transcript.get_gpa()}"

    dept.add_student(s1)
    dept.add_course(c1)
    dept.add_course(c2)

    assert len(dept.students) == 1
    assert len(dept.courses) == 2

    print("All tests passed successfully! Composition and aggregation relationships working cleanly.")
