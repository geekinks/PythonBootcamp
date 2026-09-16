import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.result import Result, Standard5PointGPAProcessor
from src.course import Course


class TestResultAndGrading(unittest.TestCase):
    def setUp(self):
        self.result = Result()
        self.courses = [
            Course("CSC301", "Python OOP", credit_units=3),
            Course("CSC305", "Databases", credit_units=4),
            Course("MTH301", "Maths", credit_units=3),
        ]

    def test_score_validation(self):
        self.result.add_score("CSC301", 85.0)
        self.assertEqual(self.result.get_score("CSC301"), 85.0)

        with self.assertRaises(ValueError):
            self.result.add_score("CSC305", 105.0)

        with self.assertRaises(ValueError):
            self.result.add_score("CSC305", -10.0)

        with self.assertRaises(TypeError):
            self.result.add_score("CSC305", "Ninety")

    def test_gpa_calculation_and_standing(self):
        # CSC301 (3 units) -> 85 (A = 5 GP) -> 15 QP
        # CSC305 (4 units) -> 65 (B = 4 GP) -> 16 QP
        # MTH301 (3 units) -> 55 (C = 3 GP) -> 9 QP
        # Total QP = 40, Total Units = 10, GPA = 4.00 (Second Class Upper)
        self.result.add_score("CSC301", 85.0)
        self.result.add_score("CSC305", 65.0)
        self.result.add_score("MTH301", 55.0)

        gpa = self.result.calculate_gpa(self.courses)
        self.assertEqual(gpa, 4.00)
        self.assertEqual(self.result.get_standing(self.courses), "Second Class Upper (2:1)")

    def test_transcript_formatting(self):
        self.result.add_score("CSC301", 90.0)
        transcript = self.result.generate_transcript("Aisha", "GSU/001", self.courses)
        self.assertIn("OFFICIAL ACADEMIC TRANSCRIPT", transcript)
        self.assertIn("Aisha", transcript)
        self.assertIn("CSC301", transcript)


if __name__ == "__main__":
    unittest.main()
