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
        self._grades = {}

    def add_grade(self, course_code: str, score: float):
        # TODO 2: Validate 0 <= score <= 100, then store in _grades
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")

        self._grades[course_code] = score

    def get_gpa(self) -> float:
        # TODO 3: Return average of scores or 0.0 if empty
        if not self._grades:
            return 0.0

        return sum(self._grades.values()) / len(self._grades)


class Student:
    def __init__(self, name: str, matric_no: str):
        self.name = name
        self.matric_no = matric_no

        # TODO 4: Composition
        self.transcript = Transcript()

    def record_score(self, course_code: str, score: float):
        # TODO 5: Delegate adding grade to transcript
        self.transcript.add_grade(course_code, score)


class Department:
    def __init__(self, name: str):
        self.name = name

        # TODO 6: Aggregation
        self.students = []
        self.courses = []

    def add_student(self, student: Student):
        # TODO 7: Append student
        self.students.append(student)

    def add_course(self, course: Course):
        # TODO 8: Append course
        self.courses.append(course)

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
