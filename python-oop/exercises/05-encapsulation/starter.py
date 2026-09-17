"""
Exercise 05: Encapsulation (Starter)
Complete the TODO items below and run this file to test your solution.
"""

class GradeBook:
    def __init__(self, student_id: str):
        self.student_id = student_id
        # TODO 1: Initialize protected attribute `_scores` as empty dict
        self.__scores = {}  # Use a protected attribute to store scores    
        pass

    def record_score(self, course_code: str, score: float):
        # TODO 2: Validate score is int or float, and 0 <= score <= 100. Raise ValueError if invalid.
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number")
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        # TODO 3: Store float(score) into self.__scores[course_code]                        
        self.__scores[course_code] = float(score)

    def get_score(self, course_code: str) -> float | None:
        # TODO 4: Return score for course_code or None if not found
        return self.__scores.get(course_code)

    @property
    def average_score(self) -> float:
        # TODO 5: Calculate and return average of all scores (or 0.0 if empty)
        if not self.__scores:
            return 0.0
        total = sum(self.__scores.values())
        return total / len(self.__scores)

    @property
    def all_scores(self) -> dict[str, float]:
        # TODO 6: Return a defensive COPY of self.__scores (.copy())
        return self.__scores.copy()


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    gb = GradeBook("GSU/CSC/001")
    assert gb.average_score == 0.0, "Empty gradebook should return 0.0 average"

    gb.record_score("CSC301", 85)
    gb.record_score("CSC305", 95)
    assert gb.get_score("CSC301") == 85.0
    assert gb.average_score == 90.0, f"Expected 90.0, got {gb.average_score}"

    # Verify out of range scores raise ValueError
    try:
        gb.record_score("MTH301", 105)
        assert False, "Should raise ValueError for score > 100"
    except ValueError:
        pass

    try:
        gb.record_score("MTH301", -5)
        assert False, "Should raise ValueError for score < 0"
    except ValueError:
        pass

    # Verify defensive copy
    tampered_copy = gb.all_scores
    tampered_copy.clear()
    assert len(gb.all_scores) == 2, "Internal dictionary leaked! Returning a copy is required."

    print("All tests passed successfully! Encapsulation and data protection verified.")
