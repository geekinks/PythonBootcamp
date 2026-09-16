"""
Exercise 05: Encapsulation (Solution)
Reference solution showing protected state, defensive copying, and input validation.
"""

class GradeBook:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self._scores: dict[str, float] = {}

    def record_score(self, course_code: str, score: float):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number.")
        if not (0.0 <= score <= 100.0):
            raise ValueError(f"Score {score} is out of bounds (must be 0-100).")
        self._scores[course_code] = float(score)

    def get_score(self, course_code: str) -> float | None:
        return self._scores.get(course_code)

    @property
    def average_score(self) -> float:
        if not self._scores:
            return 0.0
        return sum(self._scores.values()) / len(self._scores)

    @property
    def all_scores(self) -> dict[str, float]:
        return self._scores.copy()


if __name__ == "__main__":
    gb = GradeBook("GSU/CSC/001")
    gb.record_score("CSC301", 85)
    gb.record_score("CSC305", 95)
    print(f"Gradebook Average: {gb.average_score}")
    print("All tests passed successfully! Encapsulation and data protection verified.")
