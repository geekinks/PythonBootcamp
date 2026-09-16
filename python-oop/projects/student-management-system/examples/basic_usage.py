"""
Student Management System Example: Basic Usage
Quick introductory walkthrough creating a student, enrolling in a course, and viewing a profile.
"""
import sys
import os

# Add parent directory to path so src package can be imported directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.course import Course
from src.student import Student


def run_basic_example():
    print("--- Basic SMS Usage Example ---")

    # 1. Create a course
    python_course = Course("CSC301", "Introduction to Python Programming", credit_units=3)
    print(f"Created Course: {python_course.display_info()}")

    # 2. Create a student
    student = Student(
        name="Aisha Muhammad",
        email="aisha@geekink.edu",
        matric_no="GSU/CSC/001",
        department="Computer Science",
        level=200,
    )

    # 3. Enroll student in course
    student.enroll_course(python_course)
    print(f"Enrolled {student.name} into {python_course.code}. Total Credits: {student.total_credits}")

    # 4. Add a score and view profile
    student.result.add_score("CSC301", 92.5)
    print("\n" + student.display_profile())


if __name__ == "__main__":
    run_basic_example()
