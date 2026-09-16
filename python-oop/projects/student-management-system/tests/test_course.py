import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.course import Course, Department


class TestCourseAndDepartment(unittest.TestCase):
    def test_course_validation(self):
        c = Course("CSC301", "Python OOP", credit_units=3)
        self.assertEqual(c.code, "CSC301")
        self.assertEqual(c.credit_units, 3)

        with self.assertRaises(ValueError):
            Course("", "Invalid Code")

        with self.assertRaises(ValueError):
            Course("CSC301", "Too Many Units", credit_units=10)

    def test_course_equality_and_hashing(self):
        c1 = Course("CSC301", "Python OOP", 3)
        c2 = Course("CSC301", "Python OOP Updated", 3)
        self.assertEqual(c1, c2)
        self.assertEqual(len({c1, c2}), 1)

    def test_department_aggregation(self):
        dept = Department("Computer Science", "CSC")
        c1 = Course("CSC301", "Python OOP", 3)
        dept.add_course(c1)
        self.assertEqual(len(dept.courses), 1)

        # Ensure defensive copying
        courses_copy = dept.courses
        courses_copy.clear()
        self.assertEqual(len(dept.courses), 1)


if __name__ == "__main__":
    unittest.main()
