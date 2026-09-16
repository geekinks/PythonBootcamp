"""
Attendance Subsystem: Session Logs, Percentages & Exam Qualification Rules
"""
from typing import Dict, List


class AttendanceTracker:
    """
    Manages session-by-session course attendance records.
    Encapsulates attendance logs and calculates qualification metrics.
    """

    def __init__(self):
        # Maps course_code -> list of boolean attendance entries (True = Present, False = Absent)
        self._records: Dict[str, List[bool]] = {}

    def mark_attendance(self, course_code: str, is_present: bool):
        """Record attendance status for a course lecture session."""
        code = course_code.strip().upper()
        if code not in self._records:
            self._records[code] = []
        self._records[code].append(bool(is_present))

    def get_course_attendance(self, course_code: str) -> Dict[str, float]:
        """
        Returns summary metrics: total sessions, present count, absent count, and percentage.
        """
        code = course_code.strip().upper()
        sessions = self._records.get(code, [])
        total = len(sessions)
        if total == 0:
            return {"total_sessions": 0, "present": 0, "absent": 0, "percentage": 0.0}

        present_count = sum(1 for status in sessions if status)
        absent_count = total - present_count
        percentage = round((present_count / total) * 100.0, 1)

        return {
            "total_sessions": total,
            "present": present_count,
            "absent": absent_count,
            "percentage": percentage,
        }

    def is_eligible_for_exam(self, course_code: str, threshold: float = 75.0) -> bool:
        """
        Determines whether the student satisfies the minimum attendance percentage (default 75%).
        """
        stats = self.get_course_attendance(course_code)
        if stats["total_sessions"] == 0:
            return True  # No sessions logged yet
        return stats["percentage"] >= threshold

    def get_summary_report(self) -> str:
        """Renders comprehensive attendance card."""
        if not self._records:
            return "No attendance records found."

        lines = ["=== Course Attendance Report ==="]
        for code, sessions in sorted(self._records.items()):
            stats = self.get_course_attendance(code)
            status = "ELIGIBLE" if stats["percentage"] >= 75.0 else "INELIGIBLE (Below 75%)"
            lines.append(
                f"  [{code}] Sessions: {stats['total_sessions']:>2} | "
                f"Attended: {stats['present']:>2} | "
                f"Rate: {stats['percentage']:>5.1f}% -> {status}"
            )
        return "\n".join(lines)
