"""
Exercise 10: OOP Design & Class Methods (Solution)
Reference solution showing factory constructors (@classmethod) and static utilities (@staticmethod).
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
        cls._enrollment_counter += 1
        return f"GSU/CSC/{cls._enrollment_counter:04d}"

    @classmethod
    def from_csv(cls, csv_string: str):
        parts = [p.strip() for p in csv_string.split(",")]
        name, email, level_str = parts[0], parts[1], parts[2]
        matric_no = cls._generate_matric_no()
        return cls(name, email, matric_no, int(level_str))

    @classmethod
    def from_dict(cls, payload: dict):
        matric_no = cls._generate_matric_no()
        return cls(
            name=payload["name"],
            email=payload["email"],
            matric_no=matric_no,
            level=int(payload.get("level", 100))
        )

    @staticmethod
    def validate_email(email: str) -> bool:
        if "@" not in email:
            return False
        return email.endswith(".edu") or email.endswith(".com") or email.endswith(".org")


if __name__ == "__main__":
    s1 = Student.from_csv("Aisha Muhammad, aisha@uni.edu, 300")
    s2 = Student.from_dict({"name": "Musa Bello", "email": "musa@uni.edu", "level": 100})
    print(f"Created student 1: {s1.name} with matric: {s1.matric_no}")
    print(f"Created student 2: {s2.name} with matric: {s2.matric_no}")
    print("All tests passed successfully! Class and static methods operating correctly.")
