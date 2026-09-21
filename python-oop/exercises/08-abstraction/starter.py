"""
Exercise 08: Abstraction (Starter)
Complete the TODO items below and run this file to test your solution.
"""
from abc import ABC, abstractmethod


class GradeCalculator(ABC):
    # TODO 1: Define abstractmethod calculate_gpa(self, scores: list[float]) -> float
    # @abstractmethod
    # def calculate_gpa(self, scores: list[float]) -> float: ...

    # TODO 2: Define abstractmethod get_standing(self, gpa: float) -> str

    # TODO 3: Implement concrete method format_report(self, student_name: str, scores: list[float]) -> str
    def format_report(self, student_name: str, scores: list[float]) -> str:
        pass


class Undergraduate5PointCalculator(GradeCalculator):
    # TODO 4: Implement calculate_gpa using 5-point scale (70+=5, 60+=4, 50+=3, 45+=2, 40+=1, else 0)
    def calculate_gpa(self, scores: list[float]) -> float:
        pass

    # TODO 5: Implement get_standing (4.5+=First Class, 3.5+=Second Class Upper, 2.4+=Second Class Lower, else Pass/Probation)
    def get_standing(self, gpa: float) -> str:
        pass


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    # 1. Verify abstract class cannot be instantiated directly
    try:
        calc = GradeCalculator()
        assert False, "GradeCalculator should not be instantiable directly!"
    except TypeError:
        pass

    ug_calc = Undergraduate5PointCalculator()
    scores = [85.0, 62.0, 75.0]  # 5 + 4 + 5 = 14 / 3 = 4.67
    gpa = ug_calc.calculate_gpa(scores)
    assert round(gpa, 2) == 4.67, f"Expected 4.67, got {gpa}"
    assert ug_calc.get_standing(gpa) == "First Class"

    report = ug_calc.format_report("Aisha", scores)
    assert report == "Report for Aisha: GPA=4.67 | Status=First Class"

    print("All tests passed successfully! Abstract base classes and concrete implementations verified.")
