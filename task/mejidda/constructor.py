"""
Exercise 03: Constructors and Self (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class Course:
    def __init__(self, code: str, title: str, credit_units: int = 3):
        # TODO 1: Initialize self.code, self.title, and self.credit_units
        self.code = code
        self.title = title
        self.credit_units = credit_units

class Student:
    def __init__(self, name: str, matric_no: str, department: str, level: int = 100):
        self.name = name
        self.matric_no = matric_no
        self.department = department
        self.level = level
        # TODO 3: Initialize self.enrolled_courses as an empty list
        self.enrolled_courses = []

    def enroll(self, course: Course):
        # TODO 4: Append course to self.enrolled_courses if not already present
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

    def total_credits(self) -> int:
        # TODO 5: Calculate and return the sum of credit_units across all enrolled courses
        return sum(course.credit_units for course in self.enrolled_courses) 


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    c1 = Course("CSC301", "Data Structures", credit_units=3)
    c2 = Course("CSC305", "Database Management Systems", credit_units=4)
    c3 = Course("GST301", "Entrepreneurship")  # uses default credit_units=3

    assert c3.credit_units == 3, "Default credit units not set to 3"

    s1 = Student("Aisha Muhammad", "GSU/CSC/001", "Computer Science")
    assert s1.level == 100, "Default student level not set to 100"

    s2 = Student("Musa Bello", "GSU/CSC/002", "Software Engineering", level=400)
    assert s2.level == 400

    s1.enroll(c1)
    s1.enroll(c2)
    s1.enroll(c1)  # duplicate check

    assert len(s1.enrolled_courses) == 2, "Duplicate course enrolled"
    assert s1.total_credits() == 7, f"Expected 7 credits, got {s1.total_credits()}"

    print("All tests passed successfully! Constructors and self implemented properly.")
