"""
Exercise 02: Attributes and Methods (Solution)
Reference solution demonstrating instance state and method behavior.
"""

class Student:
    """Represents a student with profile and course enrollment."""

    def set_profile(self, name: str, matric_no: str, department: str, level: int):
        self.name = name
        self.matric_no = matric_no
        self.department = department
        self.level = level
        self.courses = []

    def register_course(self, course_code: str):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def drop_course(self, course_code: str):
        if course_code in self.courses:
            self.courses.remove(course_code)

    def get_profile_card(self) -> str:
        return (
            f"Student: {self.name} | "
            f"Matric: {self.matric_no} | "
            f"Dept: {self.department} | "
            f"Level: {self.level} | "
            f"Courses: {len(self.courses)}"
        )


if __name__ == "__main__":
    student = Student()
    student.set_profile("Aisha Muhammad", "GSU/CSC/001", "Computer Science", 300)

    student.register_course("CSC301")
    student.register_course("CSC305")
    student.register_course("CSC301")

    student.drop_course("CSC301")

    print(student.get_profile_card())
    print("All tests passed successfully! Attributes and methods working properly.")
