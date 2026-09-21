"""
Exercise 02: Attributes and Methods (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class Student:
    """Represents a student with profile and course enrollment."""

    def set_profile(self, name: str, matric_no: str, department: str, level: int):
        # TODO 1: Set instance attributes for name, matric_no, department, and level
        # TODO 2: Initialize self.courses as an empty list
        pass

    def register_course(self, course_code: str):
        # TODO 3: Add course_code to self.courses only if it is not already in the list
        pass

    def drop_course(self, course_code: str):
        # TODO 4: Remove course_code from self.courses if it exists in the list
        pass

    def get_profile_card(self) -> str:
        # TODO 5: Return formatted string:
        # "Student: <name> | Matric: <matric_no> | Dept: <department> | Level: <level> | Courses: <count>"
        pass


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    student = Student()
    student.set_profile("Aisha Muhammad", "GSU/CSC/001", "Computer Science", 300)

    assert student.name == "Aisha Muhammad", "Name attribute not set correctly"
    assert student.matric_no == "GSU/CSC/001", "Matric attribute not set correctly"
    assert student.department == "Computer Science", "Department attribute not set correctly"
    assert student.level == 300, "Level attribute not set correctly"
    assert student.courses == [], "Courses list should be initially empty"

    student.register_course("CSC301")
    student.register_course("CSC305")
    student.register_course("CSC301")  # Duplicate test

    assert len(student.courses) == 2, "Duplicate course was added or courses not stored"
    assert "CSC301" in student.courses and "CSC305" in student.courses

    student.drop_course("CSC301")
    assert "CSC301" not in student.courses, "Course was not dropped"
    assert len(student.courses) == 1

    expected_card = "Student: Aisha Muhammad | Matric: GSU/CSC/001 | Dept: Computer Science | Level: 300 | Courses: 1"
    assert student.get_profile_card() == expected_card, f"Card mismatch: {student.get_profile_card()}"

    print("All tests passed successfully! Attributes and methods working properly.")
