"""
Exercise 10: OOP Design & Class Methods (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class Student:
    _enrollment_counter = 0
    TOTAL_CAPACITY = 1000

    def __init__(self, name: str, email: str, matric_no: str, level: int):
        self.name = name
        self.email = email
        self.matric_no = matric_no
        self.level = level

    @classmethod
    def _generate_matric_no(cls) -> str:
        # TODO 1: Increment cls._enrollment_counter by 1 and return formatted string "GSU/CSC/{counter:04d}"
        pass

    @classmethod
    def from_csv(cls, csv_string: str):
        # TODO 2: Parse comma-separated "Name, Email, Level"
        # Generate matric using cls._generate_matric_no()
        # Return new cls instance
        pass

    @classmethod
    def from_dict(cls, payload: dict):
        # TODO 3: Parse dictionary payload, generate matric number, and return new cls instance
        pass

    @staticmethod
    def validate_email(email: str) -> bool:
        # TODO 4: Return True if email contains '@' and ends with ('.edu' or '.com'), else False
        pass


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    assert Student.validate_email("aisha@uni.edu") is True
    assert Student.validate_email("invalid_address") is False

    s1 = Student.from_csv("Aisha Muhammad, aisha@uni.edu, 300")
    assert s1.name == "Aisha Muhammad"
    assert s1.matric_no == "GSU/CSC/0001"
    assert s1.level == 300

    s2 = Student.from_dict({"name": "Musa Bello", "email": "musa@uni.edu", "level": 100})
    assert s2.name == "Musa Bello"
    assert s2.matric_no == "GSU/CSC/0002"

    assert Student._enrollment_counter == 2

    print("All tests passed successfully! Class and static methods operating correctly.")
