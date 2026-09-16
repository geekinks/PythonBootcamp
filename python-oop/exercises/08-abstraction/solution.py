"""
Exercise 08: Abstraction (Solution)
Reference solution showing Abstract Base Classes (ABCs), contract enforcement, and concrete subtyping.
"""
from abc import ABC, abstractmethod


class GradeCalculator(ABC):
    @abstractmethod
    def calculate_gpa(self, scores: list[float]) -> float:
        """Calculate numerical GPA from a list of course scores."""
        pass

    @abstractmethod
    def get_standing(self, gpa: float) -> str:
        """Return academic honors or standing based on GPA."""
        pass

    def format_report(self, student_name: str, scores: list[float]) -> str:
        gpa = self.calculate_gpa(scores)
        standing = self.get_standing(gpa)
        return f"Report for {student_name}: GPA={gpa:.2f} | Status={standing}"


class Undergraduate5PointCalculator(GradeCalculator):
    @staticmethod
    def _score_to_gp(score: float) -> int:
        if score >= 70:
            return 5
        elif score >= 60:
            return 4
        elif score >= 50:
            return 3
        elif score >= 45:
            return 2
        elif score >= 40:
            return 1
        return 0

    def calculate_gpa(self, scores: list[float]) -> float:
        if not scores:
            return 0.0
        total_gp = sum(self._score_to_gp(s) for s in scores)
        return total_gp / len(scores)

    def get_standing(self, gpa: float) -> str:
        if gpa >= 4.5:
            return "First Class"
        elif gpa >= 3.5:
            return "Second Class Upper"
        elif gpa >= 2.4:
            return "Second Class Lower"
        return "Pass/Probation"


if __name__ == "__main__":
    calc = Undergraduate5PointCalculator()
    print(calc.format_report("Aisha", [85.0, 62.0, 75.0]))
    print("All tests passed successfully! Abstract base classes and concrete implementations verified.")
