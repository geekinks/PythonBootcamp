"""
Exercise 04: Properties (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class StudentProfile:
    def __init__(self, first_name: str, last_name: str, email: str, cgpa: float = 0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cgpa = cgpa  # invoke setter

    # TODO 1: Implement full_name getter property
    # @property
    # def full_name(self) -> str: ...
@property
def full_name(self) -> str:
    return f"{self.first_name} {self.last_name}"

    # TODO 2: Implement full_name setter (split into first_name and last_name)
    @full_name.setter
    def full_name(self, value: str):
        names = value.split()
        self.first_name = names[0]
        self.last_name = names[1] if len(names) > 1 else ""

    # TODO 3: Implement cgpa getter and setter (enforcing 0.0 <= cgpa <= 5.0, else raise ValueError)
    @property
    def cgpa(self) -> float:
        return self._cgpa

    @cgpa.setter
    def cgpa(self, value: float):
        if not (0.0 <= value <= 5.0):
            raise ValueError("CGPA must be between 0.0 and 5.0")
        self._cgpa = value

    # TODO 4: Implement read-only academic_standing property based on cgpa ranges
    @property
    def academic_standing(self) -> str:
        if self.cgpa >= 4.5:
            return "First Class"
        elif self.cgpa >= 4.0:
            return "Second Class Upper"
        elif self.cgpa >= 3.5:
            return "Second Class Lower"
        else:
            return "Pass"

# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    profile = StudentProfile("Aisha", "Muhammad", "aisha@uni.edu", 4.75)

    assert profile.full_name == "Aisha Muhammad", "full_name getter incorrect"
    assert profile.academic_standing == "First Class", "academic_standing calculation incorrect"

    # Test full_name setter
    profile.full_name = "Fatima Bello"
    assert profile.first_name == "Fatima" and profile.last_name == "Bello"
    assert profile.full_name == "Fatima Bello"

    # Test cgpa validation
    profile.cgpa = 3.80
    assert profile.academic_standing == "Second Class Upper"

    profile.cgpa = 2.80
    assert profile.academic_standing == "Second Class Lower"

    try:
        profile.cgpa = 5.50
        assert False, "Should have raised ValueError for CGPA > 5.0"
    except ValueError:
        pass

    try:
        profile.cgpa = -1.0
        assert False, "Should have raised ValueError for negative CGPA"
    except ValueError:
        pass

    print("All tests passed successfully! Properties and setters work correctly.")
