"""
Academic Catalog Subsystem: Course & Department Entities
"""
from typing import List


class Course:
    """
    Represents an individual academic course module.
    Encapsulates course code, descriptive title, credit weighting, and department association.
    """

    def __init__(self, code: str, title: str, credit_units: int = 3, department: str = "Computer Science"):
        if not code or not isinstance(code, str):
            raise ValueError("Course code must be a non-empty string.")
        if not (1 <= credit_units <= 6):
            raise ValueError(f"Credit units must be between 1 and 6, received: {credit_units}")

        self._code = code.strip().upper()
        self._title = title.strip()
        self._credit_units = int(credit_units)
        self._department = department.strip()

    @property
    def code(self) -> str:
        return self._code

    @property
    def title(self) -> str:
        return self._title

    @property
    def credit_units(self) -> int:
        return self._credit_units

    @property
    def department(self) -> str:
        return self._department

    def display_info(self) -> str:
        return f"[{self._code}] {self._title} ({self._credit_units} Credit Units) - Dept: {self._department}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Course):
            return self._code == other.code
        return False

    def __hash__(self) -> int:
        return hash(self._code)

    def __repr__(self) -> str:
        return f"<Course {self._code}: '{self._title}'>"


class Department:
    """
    Represents an academic department aggregating faculty members, courses, and students.
    """

    def __init__(self, name: str, code: str):
        self._name = name.strip()
        self._code = code.strip().upper()
        self._courses: List[Course] = []
        self._faculty: List = []
        self._students: List = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def code(self) -> str:
        return self._code

    @property
    def courses(self) -> List[Course]:
        """Defensive copy of registered courses."""
        return self._courses.copy()

    def add_course(self, course: Course):
        if not isinstance(course, Course):
            raise TypeError("Expected an instance of Course.")
        if course not in self._courses:
            self._courses.append(course)

    def add_faculty(self, lecturer):
        if lecturer not in self._faculty:
            self._faculty.append(lecturer)

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def get_summary(self) -> str:
        return (
            f"=== Department of {self._name} ({self._code}) ===\n"
            f"Offered Courses:   {len(self._courses)}\n"
            f"Teaching Faculty:  {len(self._faculty)}\n"
            f"Enrolled Students: {len(self._students)}"
        )
