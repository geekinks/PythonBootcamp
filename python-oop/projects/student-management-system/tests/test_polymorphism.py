import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.user import User
from src.student import Student
from src.lecturer import Lecturer


class TestPolymorphismAndHierarchy(unittest.TestCase):
    def setUp(self):
        self.student = Student("Aisha Muhammad", "aisha@geekink.edu", "GSU/001", level=300)
        self.lecturer = Lecturer("Dr. Kabir", "kabir@geekink.edu", "STF-014", "CSC")

    def test_inheritance_types(self):
        self.assertTrue(isinstance(self.student, User))
        self.assertTrue(isinstance(self.lecturer, User))
        self.assertTrue(issubclass(Student, User))
        self.assertTrue(issubclass(Lecturer, User))

    def test_polymorphic_display_profile(self):
        users = [self.student, self.lecturer]
        profiles = [u.display_profile() for u in users]

        self.assertEqual(len(profiles), 2)
        self.assertIn("Student Profile", profiles[0])
        self.assertIn("Aisha Muhammad", profiles[0])

        self.assertIn("Faculty Profile", profiles[1])
        self.assertIn("Dr. Kabir", profiles[1])

    def test_inherited_notification_behavior(self):
        msg1 = self.student.send_notification("Exam starting tomorrow")
        msg2 = self.lecturer.send_notification("Senate meeting at 2pm")

        self.assertIn("aisha@geekink.edu", msg1)
        self.assertIn("kabir@geekink.edu", msg2)


if __name__ == "__main__":
    unittest.main()
