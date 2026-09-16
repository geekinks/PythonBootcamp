"""
Student Management System (SMS) Package
Demonstrating clean OOP architecture, design patterns, and domain modeling in Python.
"""

from .user import User
from .course import Course, Department
from .result import Result, ResultProcessor, Standard5PointGPAProcessor
from .attendance import AttendanceTracker
from .student import Student
from .lecturer import Lecturer

__all__ = [
    "User",
    "Course",
    "Department",
    "Result",
    "ResultProcessor",
    "Standard5PointGPAProcessor",
    "AttendanceTracker",
    "Student",
    "Lecturer",
]
