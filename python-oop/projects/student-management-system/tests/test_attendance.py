import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.attendance import AttendanceTracker


class TestAttendance(unittest.TestCase):
    def setUp(self):
        self.tracker = AttendanceTracker()

    def test_attendance_logging_and_percentages(self):
        for _ in range(8):
            self.tracker.mark_attendance("CSC301", is_present=True)
        for _ in range(2):
            self.tracker.mark_attendance("CSC301", is_present=False)

        stats = self.tracker.get_course_attendance("CSC301")
        self.assertEqual(stats["total_sessions"], 10)
        self.assertEqual(stats["present"], 8)
        self.assertEqual(stats["absent"], 2)
        self.assertEqual(stats["percentage"], 80.0)

    def test_exam_eligibility(self):
        # 80% attendance -> Eligible
        for _ in range(8):
            self.tracker.mark_attendance("CSC301", True)
        for _ in range(2):
            self.tracker.mark_attendance("CSC301", False)
        self.assertTrue(self.tracker.is_eligible_for_exam("CSC301", threshold=75.0))

        # 50% attendance -> Ineligible
        self.tracker.mark_attendance("CSC305", True)
        self.tracker.mark_attendance("CSC305", False)
        self.assertFalse(self.tracker.is_eligible_for_exam("CSC305", threshold=75.0))


if __name__ == "__main__":
    unittest.main()
