import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.student import Student
from src.course import Course


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(
            name="Aisha Muhammad",
            email="aisha@geekink.edu",
            matric_no="GSU/CSC/001",
            department="Computer Science",
            level=300,
        )
        self.course1 = Course("CSC301", "Python OOP", credit_units=3)
        self.course2 = Course("CSC305", "Databases", credit_units=4)

    def test_student_initialization(self):
        self.assertEqual(self.student.name, "Aisha Muhammad")
        self.assertEqual(self.student.email, "aisha@geekink.edu")
        self.assertEqual(self.student.matric_no, "GSU/CSC/001")
        self.assertEqual(self.student.level, 300)
        self.assertEqual(self.student.total_credits, 0)

    def test_invalid_email_raises_value_error(self):
        with self.assertRaises(ValueError):
            Student("Test", "invalid-email-string", "GSU/002")

    def test_level_validation(self):
        self.student.level = 400
        self.assertEqual(self.student.level, 400)
        with self.assertRaises(ValueError):
            self.student.level = 999

    def test_course_enrollment_and_drop(self):
        self.assertTrue(self.student.enroll_course(self.course1))
        self.assertTrue(self.student.enroll_course(self.course2))
        self.assertFalse(self.student.enroll_course(self.course1))  # Duplicate

        self.assertEqual(len(self.student.enrolled_courses), 2)
        self.assertEqual(self.student.total_credits, 7)

        self.assertTrue(self.student.drop_course("CSC301"))
        self.assertEqual(len(self.student.enrolled_courses), 1)
        self.assertEqual(self.student.total_credits, 4)

    def test_promotion(self):
        self.assertEqual(self.student.promote(), 400)
        self.assertEqual(self.student.promote(), 500)
        with self.assertRaises(ValueError):
            self.student.promote()


if __name__ == "__main__":
    unittest.main()
