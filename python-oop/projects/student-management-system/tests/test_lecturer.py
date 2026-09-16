import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.lecturer import Lecturer
from src.student import Student
from src.course import Course


class TestLecturer(unittest.TestCase):
    def setUp(self):
        self.lecturer = Lecturer(
            name="Dr. Kabir Ibrahim",
            email="kabir@geekink.edu",
            staff_id="STF-014",
            department_name="Computer Science",
        )
        self.student = Student("Aisha", "aisha@geekink.edu", "GSU/001")
        self.course = Course("CSC301", "Python OOP", 3)

    def test_lecturer_initialization(self):
        self.assertEqual(self.lecturer.name, "Dr. Kabir Ibrahim")
        self.assertEqual(self.lecturer.staff_id, "STF-014")
        self.assertEqual(self.lecturer.assigned_courses, [])

    def test_course_assignment(self):
        self.assertTrue(self.lecturer.assign_course(self.course))
        self.assertFalse(self.lecturer.assign_course(self.course))  # duplicate
        self.assertEqual(len(self.lecturer.assigned_courses), 1)

    def test_score_submission_authorization(self):
        # Lecturer not assigned to course -> PermissionError
        with self.assertRaises(PermissionError):
            self.lecturer.submit_score(self.student, self.course, 85.0)

        # Assign course to lecturer
        self.lecturer.assign_course(self.course)

        # Student not enrolled -> ValueError
        with self.assertRaises(ValueError):
            self.lecturer.submit_score(self.student, self.course, 85.0)

        # Student enrolls -> Success
        self.student.enroll_course(self.course)
        self.assertTrue(self.lecturer.submit_score(self.student, self.course, 85.0))
        self.assertEqual(self.student.result.get_score("CSC301"), 85.0)


if __name__ == "__main__":
    unittest.main()
