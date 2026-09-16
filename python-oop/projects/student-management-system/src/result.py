"""
Evaluation Subsystem: Result, Grading Contracts (ABC), and GPA Processing Strategies
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from .course import Course


class ResultProcessor(ABC):
    """
    Abstract Strategy defining the interface for grading systems and GPA calculation.
    Enables pluggable grading scales (5.0 Nigerian/US scale, 4.0 scale, Percentage scale).
    """

    @abstractmethod
    def score_to_grade_point(self, score: float) -> int:
        """Convert a percentage score (0-100) to a numeric Grade Point (GP)."""
        pass

    @abstractmethod
    def score_to_letter_grade(self, score: float) -> str:
        """Convert a percentage score (0-100) to a Letter Grade."""
        pass

    @abstractmethod
    def calculate_gpa(self, scores: Dict[str, float], courses: List[Course]) -> float:
        """Calculate weighted Grade Point Average based on course credit units."""
        pass

    @abstractmethod
    def determine_standing(self, gpa: float) -> str:
        """Classify academic honors or standing based on GPA."""
        pass


class Standard5PointGPAProcessor(ResultProcessor):
    """
    Standard Nigerian / 5.0 Scale University Grading Processor:
    - 70-100: A (5 Points) -> First Class (4.50 - 5.00)
    - 60-69:  B (4 Points) -> Second Class Upper (3.50 - 4.49)
    - 50-59:  C (3 Points) -> Second Class Lower (2.40 - 3.49)
    - 45-49:  D (2 Points) -> Third Class (1.50 - 2.39)
    - 40-44:  E (1 Point)  -> Pass (1.00 - 1.49)
    - 0-39:   F (0 Points) -> Fail / Probation (< 1.00)
    """

    def score_to_grade_point(self, score: float) -> int:
        if score >= 70.0:
            return 5
        elif score >= 60.0:
            return 4
        elif score >= 50.0:
            return 3
        elif score >= 45.0:
            return 2
        elif score >= 40.0:
            return 1
        return 0

    def score_to_letter_grade(self, score: float) -> str:
        if score >= 70.0:
            return "A"
        elif score >= 60.0:
            return "B"
        elif score >= 50.0:
            return "C"
        elif score >= 45.0:
            return "D"
        elif score >= 40.0:
            return "E"
        return "F"

    def calculate_gpa(self, scores: Dict[str, float], courses: List[Course]) -> float:
        if not scores or not courses:
            return 0.0

        credits_lookup = {c.code: c.credit_units for c in courses}
        total_quality_points = 0
        total_credit_units = 0

        for course_code, score in scores.items():
            if course_code in credits_lookup:
                credit = credits_lookup[course_code]
                gp = self.score_to_grade_point(score)
                total_quality_points += (gp * credit)
                total_credit_units += credit

        if total_credit_units == 0:
            return 0.0

        return round(total_quality_points / total_credit_units, 2)

    def determine_standing(self, gpa: float) -> str:
        if gpa >= 4.50:
            return "First Class Honours"
        elif gpa >= 3.50:
            return "Second Class Upper (2:1)"
        elif gpa >= 2.40:
            return "Second Class Lower (2:2)"
        elif gpa >= 1.50:
            return "Third Class"
        elif gpa >= 1.00:
            return "Pass"
        return "Probation / Fail"


class Result:
    """
    Manages academic scores and transcript generation for a student.
    Composed inside the Student entity.
    """

    def __init__(self, processor: Optional[ResultProcessor] = None):
        self._scores: Dict[str, float] = {}
        # Dependency Inversion: defaults to Standard5PointGPAProcessor but accepts any ResultProcessor
        self._processor: ResultProcessor = processor or Standard5PointGPAProcessor()

    @property
    def processor(self) -> ResultProcessor:
        return self._processor

    @processor.setter
    def processor(self, new_processor: ResultProcessor):
        if not isinstance(new_processor, ResultProcessor):
            raise TypeError("Expected instance of ResultProcessor.")
        self._processor = new_processor

    @property
    def all_scores(self) -> Dict[str, float]:
        """Defensive copy of scores dictionary."""
        return self._scores.copy()

    def add_score(self, course_code: str, score: float):
        """Validates score boundaries and stores score."""
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a numeric value.")
        if not (0.0 <= score <= 100.0):
            raise ValueError(f"Score {score} is invalid. Must be between 0.0 and 100.0.")

        self._scores[course_code.strip().upper()] = float(score)

    def get_score(self, course_code: str) -> Optional[float]:
        return self._scores.get(course_code.strip().upper())

    def calculate_gpa(self, courses: List[Course]) -> float:
        return self._processor.calculate_gpa(self._scores, courses)

    def get_standing(self, courses: List[Course]) -> str:
        gpa = self.calculate_gpa(courses)
        return self._processor.determine_standing(gpa)

    def generate_transcript(self, student_name: str, matric_no: str, courses: List[Course]) -> str:
        """Renders formatted academic transcript."""
        course_map = {c.code: c for c in courses}
        lines = [
            "=" * 65,
            f"             OFFICIAL ACADEMIC TRANSCRIPT",
            "=" * 65,
            f" Student Name: {student_name}",
            f" Matric No:    {matric_no}",
            "-" * 65,
            f" {'Course':<10} | {'Units':<5} | {'Score':<6} | {'Grade':<5} | {'Points':<6}",
            "-" * 65,
        ]

        for code, score in sorted(self._scores.items()):
            course = course_map.get(code)
            units = course.credit_units if course else 3
            letter = self._processor.score_to_letter_grade(score)
            gp = self._processor.score_to_grade_point(score)
            qp = gp * units
            lines.append(f" {code:<10} | {units:<5} | {score:<6.1f} | {letter:<5} | {qp:<6}")

        gpa = self.calculate_gpa(courses)
        standing = self.get_standing(courses)

        lines.extend([
            "-" * 65,
            f" Cumulative GPA:    {gpa:.2f} / 5.00",
            f" Academic Standing: {standing}",
            "=" * 65,
        ])
        return "\n".join(lines)
