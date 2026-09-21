"""
Exercise 06: Inheritance (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class User:
    def __init__(self, name: str, email: str):
        # TODO 1: Initialize self.name and self.email
        self.name=name
        self.email=email 
        pass

    def get_role(self) -> str:
        # TODO 2: Return default role string "User"
        return "User"
    def format_header(self) -> str:
        return f"[{self.get_role()}] {self.name} <{self.email}>"


class Student(User):
    def __init__(self, name: str, email: str, matric_no: str, level: int = 100):
        # TODO 3: Call super().__init__(name, email)
        super().__init__(name, email)
        # TODO 4: Initialize self.matric_no and self.level
        self.matric_no = matric_no
        self.level = level

    def get_role(self) -> str:
        # TODO 5: Override to return "Student"
        return "Student"


class Lecturer(User):
    def __init__(self, name: str, email: str, staff_id: str, department: str):
        # TODO 6: Call super().__init__(name, email)
        super().__init__(name, email)
        # TODO 7: Initialize self.staff_id and self.department
        self.staff_id = staff_id
        self.department = department

    def get_role(self) -> str:
        # TODO 8: Override to return "Lecturer"
        return "Lecturer"
        pass


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    student = Student("Aisha Muhammad", "aisha@uni.edu", "GSU/CSC/001", 300)
    lecturer = Lecturer("Dr. Kabir", "kabir@uni.edu", "STF-402", "Computer Science")

    assert isinstance(student, User), "Student must inherit from User"
    assert isinstance(lecturer, User), "Lecturer must inherit from User"

    assert student.matric_no == "GSU/CSC/001"
    assert lecturer.department == "Computer Science"

    assert student.get_role() == "Student"
    assert lecturer.get_role() == "Lecturer"

    assert student.format_header() == "[Student] Aisha Muhammad <aisha@uni.edu>"
    assert lecturer.format_header() == "[Lecturer] Dr. Kabir <kabir@uni.edu>"

    print("All tests passed successfully! Inheritance hierarchy functioning as expected.")
