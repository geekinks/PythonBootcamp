"""
Faculty Subsystem: Lecturer Entity (Inheriting User & Associating with Courses & Students)
"""
from typing import List
from .user import User
from .course import Course
from .student import Student


class Lecturer(User):
    """
    Represents an academic faculty member.
    Inherits from User (IS-A).
    Associates with Course (TEACHES) and Student (ASSESSES).
    """

    def __init__(
        self,
        name: str,
        email: str,
        staff_id: str,
        department_name: str = "Computer Science",
        academic_rank: str = "Senior Lecturer",
    ):
        super().__init__(name=name, email=email, user_id=staff_id)
        self._staff_id = staff_id.strip()
        self._department_name = department_name.strip()
        self._academic_rank = academic_rank.strip()
        self._assigned_courses: List[Course] = []

    @property
    def staff_id(self) -> str:
        return self._staff_id

    @property
    def department_name(self) -> str:
        return self._department_name

    @property
    def academic_rank(self) -> str:
        return self._academic_rank

    @property
    def assigned_courses(self) -> List[Course]:
        """Defensive copy of assigned teaching courses."""
        return self._assigned_courses.copy()

    def assign_course(self, course: Course) -> bool:
        """Assigns a course to the lecturer's teaching workload."""
        if not isinstance(course, Course):
            raise TypeError("Expected an instance of Course.")
        if course not in self._assigned_courses:
            self._assigned_courses.append(course)
            return True
        return False

    def submit_score(self, student: Student, course: Course, score: float) -> bool:
        """
        Submits student score for a course taught by this lecturer.
        Validates authorization (lecturer must teach course, student must be enrolled).
        """
        if not isinstance(student, Student):
            raise TypeError("Expected an instance of Student.")
        if not isinstance(course, Course):
            raise TypeError("Expected an instance of Course.")

        if course not in self._assigned_courses:
            raise PermissionError(f"Lecturer {self.name} is not assigned to teach {course.code}.")

        if course not in student.enrolled_courses:
            raise ValueError(f"Student {student.name} is not enrolled in {course.code}.")

        student.result.add_score(course.code, score)
        return True

    def display_profile(self) -> str:
        """Polymorphic implementation of User.display_profile()."""
        teaching = ", ".join(c.code for c in self._assigned_courses) or "No assigned courses"
        return (
            f"=== Faculty Profile ===\n"
            f"  Name:       {self.name} ({self._academic_rank})\n"
            f"  Email:      {self.email}\n"
            f"  Staff ID:   {self.staff_id}\n"
            f"  Department: {self.department_name}\n"
            f"  Teaching:   [{teaching}]"
        )
