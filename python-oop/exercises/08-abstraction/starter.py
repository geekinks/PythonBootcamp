"""
Exercise 08: Abstraction (Starter)
Complete the TODO items below and run this file to test your solution.
"""
from abc import ABC, abstractmethod


class GradeCalculator(ABC):

    # TODO 1: Abstract method
    @abstractmethod
    def calculate_gpa(self, scores: list[float]) -> float:
        pass

    # TODO 2: Abstract method
    @abstractmethod
    def get_standing(self, gpa: float) -> str:
        pass

    # TODO 3: Concrete method
    def format_report(self, student_name: str, scores: list[float]) -> str:
        gpa = self.calculate_gpa(scores)
        standing = self.get_standing(gpa)

        return f"Student: {student_name}\nGPA: {gpa:.2f}\nStanding: {standing}"


class Undergraduate5PointCalculator(GradeCalculator):

    # TODO 4: Calculate GPA using 5-point scale
    def calculate_gpa(self, scores: list[float]) -> float:
        if not scores:
            return 0.0

        total_points = 0

        for score in scores:
            if score >= 70:
                total_points += 5
            elif score >= 60:
                total_points += 4
            elif score >= 50:
                total_points += 3
            elif score >= 45:
                total_points += 2
            elif score >= 40:
                total_points += 1
            else:
                total_points += 0

        return total_points / len(scores)

    # TODO 5: Get student's standing
    def get_standing(self, gpa: float) -> str:
        if gpa >= 4.5:
            return "First Class"
        elif gpa >= 3.5:
            return "Second Class Upper"
        elif gpa >= 2.4:
            return "Second Class Lower"
        else:
            return "Pass/Probation"
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
    assert report == "Student: Aisha\nGPA: 4.67\nStanding: First Class"

    print("All tests passed successfully! Abstract base classes and concrete implementations verified.")
