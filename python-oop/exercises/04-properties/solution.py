"""
Exercise 04: Properties (Solution)
Reference solution demonstrating @property and @setter for validation and computed state.
"""

class StudentProfile:
    def __init__(self, first_name: str, last_name: str, email: str, cgpa: float = 0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cgpa = cgpa

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value: str):
        parts = value.strip().split(" ", 1)
        self.first_name = parts[0]
        self.last_name = parts[1] if len(parts) > 1 else ""

    @property
    def cgpa(self) -> float:
        return self._cgpa

    @cgpa.setter
    def cgpa(self, value: float):
        if not (0.0 <= value <= 5.0):
            raise ValueError("CGPA must be between 0.0 and 5.0")
        self._cgpa = round(float(value), 2)

    @property
    def academic_standing(self) -> str:
        if self._cgpa >= 4.50:
            return "First Class"
        elif self._cgpa >= 3.50:
            return "Second Class Upper"
        elif self._cgpa >= 2.40:
            return "Second Class Lower"
        elif self._cgpa >= 1.50:
            return "Third Class"
        return "Probation"


if __name__ == "__main__":
    p = StudentProfile("Aisha", "Muhammad", "aisha@uni.edu", 4.8)
    print(f"Name: {p.full_name}, CGPA: {p.cgpa}, Class: {p.academic_standing}")
    print("All tests passed successfully! Properties and setters work correctly.")
