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
        # TODO 1: Increment counter and generate matric number
        cls._enrollment_counter += 1
        return f"GSU/CSC/{cls._enrollment_counter:04d}"

    @classmethod
    def from_csv(cls, csv_string: str):
        # TODO 2: Parse "Name, Email, Level"
        name, email, level = csv_string.split(",")

        # Remove extra spaces
        name = name.strip()
        email = email.strip()
        level = int(level.strip())

        # Generate matric number
        matric_no = cls._generate_matric_no()

        # Return a new Student object
        return cls(name, email, matric_no, level)

    @classmethod
    def from_dict(cls, payload: dict):
        # TODO 3: Parse dictionary payload
        name = payload["name"]
        email = payload["email"]
        level = payload["level"]

        # Generate matric number
        matric_no = cls._generate_matric_no()

        # Return a new Student object
        return cls(name, email, matric_no, level)

    @staticmethod
    def validate_email(email: str) -> bool:
        # TODO 4: Check email format
        return "@" in email and (
            email.endswith(".edu") or email.endswith(".com")
        )
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
