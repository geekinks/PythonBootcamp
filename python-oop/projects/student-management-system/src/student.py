"""
Student Subsystem: Student Entity (Inheriting User & Composing Result & Attendance)
"""
from typing import List
from .user import User
from .course import Course
from .result import Result
from .attendance import AttendanceTracker


class Student(User):
    """
    Represents an enrolled undergraduate or postgraduate student.
    Inherits identity from User (IS-A).
    Composes Result and AttendanceTracker (HAS-A).
    Aggregates Course objects (REFERENCES).
    """

    VALID_LEVELS = {100, 200, 300, 400, 500}

    def __init__(
        self,
        name: str,
        email: str,
        matric_no: str,
        department: str = "Computer Science",
        level: int = 100,
    ):
        super().__init__(name=name, email=email, user_id=matric_no)
        self._matric_no = matric_no.strip()
        self._department = department.strip()
        self.level = level  # validated via property setter

        self._enrolled_courses: List[Course] = []
        # Object Composition: Student owns a dedicated Result and AttendanceTracker instance
        self.result = Result()
        self.attendance = AttendanceTracker()

    @property
    def matric_no(self) -> str:
        return self._matric_no

    @property
    def department(self) -> str:
        return self._department

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int) or value not in self.VALID_LEVELS:
            raise ValueError(f"Invalid level: {value}. Allowed levels: {sorted(self.VALID_LEVELS)}")
        self._level = value

    @property
    def enrolled_courses(self) -> List[Course]:
        """Defensive copy of enrolled course collection."""
        return self._enrolled_courses.copy()

    @property
    def total_credits(self) -> int:
        """Computed property: total credit units across all enrolled courses."""
        return sum(c.credit_units for c in self._enrolled_courses)

    def enroll_course(self, course: Course) -> bool:
        """Enrolls in course if not already enrolled."""
        if not isinstance(course, Course):
            raise TypeError("Expected an instance of Course.")
        if course in self._enrolled_courses:
            return False
        self._enrolled_courses.append(course)
        return True

    def drop_course(self, course_code: str) -> bool:
        """Drops course by code."""
        code = course_code.strip().upper()
        for course in self._enrolled_courses:
            if course.code == code:
                self._enrolled_courses.remove(course)
                return True
        return False

    def promote(self) -> int:
        """Promotes student to next academic level if below 500."""
        next_level = self._level + 100
        if next_level in self.VALID_LEVELS:
            self._level = next_level
            return self._level
        raise ValueError(f"Cannot promote student beyond level {self._level} (Graduation status reached).")

    def display_profile(self) -> str:
        """Polymorphic implementation of User.display_profile()."""
        gpa = self.result.calculate_gpa(self._enrolled_courses)
        standing = self.result.get_standing(self._enrolled_courses)
        course_codes = ", ".join(c.code for c in self._enrolled_courses) or "No courses enrolled"

        return (
            f"=== Student Profile ===\n"
            f"  Full Name:   {self.name}\n"
            f"  Email:       {self.email}\n"
            f"  Matric No:   {self.matric_no}\n"
            f"  Department:  {self.department}\n"
            f"  Level:       {self.level}\n"
            f"  Credits:     {self.total_credits} Units\n"
            f"  Courses:     [{course_codes}]\n"
            f"  Current GPA: {gpa:.2f} ({standing})"
        )
