"""
Student Management System Example: Advanced Workflow
Demonstrates custom ResultProcessor injection, exam eligibility check, and bulk grading.
"""
import sys
import os

# Add parent directory to path so src package can be imported directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.course import Course, Department
from src.student import Student
from src.lecturer import Lecturer
from src.result import ResultProcessor


# Demonstration of Open/Closed Principle: Custom 4.0 GPA Grading Scale Plugin
class US4PointGPAProcessor(ResultProcessor):
    """Custom plug-in processor implementing a 4.0 GPA scale."""

    def score_to_grade_point(self, score: float) -> int:
        if score >= 90.0:
            return 4  # A
        elif score >= 80.0:
            return 3  # B
        elif score >= 70.0:
            return 2  # C
        elif score >= 60.0:
            return 1  # D
        return 0      # F

    def score_to_letter_grade(self, score: float) -> str:
        if score >= 90.0: return "A"
        if score >= 80.0: return "B"
        if score >= 70.0: return "C"
        if score >= 60.0: return "D"
        return "F"

    def calculate_gpa(self, scores: dict, courses: list) -> float:
        if not scores or not courses:
            return 0.0
        lookup = {c.code: c.credit_units for c in courses}
        qp, units = 0, 0
        for code, score in scores.items():
            if code in lookup:
                u = lookup[code]
                qp += self.score_to_grade_point(score) * u
                units += u
        return round(qp / units, 2) if units > 0 else 0.0

    def determine_standing(self, gpa: float) -> str:
        if gpa >= 3.8:
            return "Summa Cum Laude"
        elif gpa >= 3.5:
            return "Magna Cum Laude"
        elif gpa >= 3.0:
            return "Dean's List"
        elif gpa >= 2.0:
            return "Good Standing"
        return "Academic Warning"


def run_advanced_workflow():
    print("--- Advanced SMS Workflow (Custom 4.0 GPA Strategy) ---")

    c1 = Course("CSC401", "Compiler Construction", 4)
    c2 = Course("CSC405", "Distributed Systems", 4)

    student = Student("Fatima Usman", "fatima@geekink.edu", "GSU/CSC/040", level=400)
    student.enroll_course(c1)
    student.enroll_course(c2)

    # Invalidate attendance for CSC405 (only 3 of 10 sessions attended)
    for _ in range(3):
        student.attendance.mark_attendance("CSC405", True)
    for _ in range(7):
        student.attendance.mark_attendance("CSC405", False)

    print(f"CSC405 Exam Eligible? {student.attendance.is_eligible_for_exam('CSC405')}")

    # Inject custom 4.0 GPA processor dynamically (Dependency Inversion)
    student.result.processor = US4PointGPAProcessor()

    student.result.add_score("CSC401", 94.0)  # 4 GP * 4 = 16
    student.result.add_score("CSC405", 82.0)  # 3 GP * 4 = 12

    print("\n" + student.result.generate_transcript(student.name, student.matric_no, student.enrolled_courses))


if __name__ == "__main__":
    run_advanced_workflow()
