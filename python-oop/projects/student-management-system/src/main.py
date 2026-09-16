"""
Student Management System: Interactive Application Entrypoint
Demonstrates end-to-end OOP domain flow: registration, enrollment, attendance, grading & transcripts.
"""
from .course import Course, Department
from .student import Student
from .lecturer import Lecturer
from .result import Standard5PointGPAProcessor


def main():
    print("=" * 70)
    print("🎓 GEEKINK INSTITUTE - STUDENT MANAGEMENT SYSTEM (SMS) 🎓")
    print("   Demonstrating Clean OOP Architecture & Domain Modeling")
    print("=" * 70)

    # 1. Setup Department & Courses
    dept_cs = Department("Computer Science & Information Technology", "CSC")

    csc301 = Course("CSC301", "Python OOP & Architecture", credit_units=3, department="CSC")
    csc305 = Course("CSC305", "Database Systems & Modeling", credit_units=4, department="CSC")
    mth301 = Course("MTH301", "Linear Algebra & Optimization", credit_units=3, department="Mathematics")

    dept_cs.add_course(csc301)
    dept_cs.add_course(csc305)
    dept_cs.add_course(mth301)

    print("\n--- 1. Department Catalog Initialized ---")
    print(dept_cs.get_summary())

    # 2. Setup Faculty Members
    dr_kabir = Lecturer(
        name="Dr. Kabir Ibrahim",
        email="k.ibrahim@geekink.edu",
        staff_id="STF-014",
        department_name="Computer Science",
        academic_rank="Associate Professor",
    )
    dr_kabir.assign_course(csc301)
    dr_kabir.assign_course(csc305)

    prof_amina = Lecturer(
        name="Prof. Amina Bello",
        email="a.bello@geekink.edu",
        staff_id="STF-003",
        department_name="Mathematics",
        academic_rank="Professor",
    )
    prof_amina.assign_course(mth301)

    dept_cs.add_faculty(dr_kabir)
    dept_cs.add_faculty(prof_amina)

    # 3. Setup Students
    aisha = Student(
        name="Aisha Muhammad",
        email="aisha.m@geekink.edu",
        matric_no="GSU/CSC/22/001",
        department="Computer Science",
        level=300,
    )
    musa = Student(
        name="Musa Bello",
        email="musa.b@geekink.edu",
        matric_no="GSU/CSC/22/002",
        department="Computer Science",
        level=300,
    )

    dept_cs.add_student(aisha)
    dept_cs.add_student(musa)

    # 4. Course Enrollment
    print("\n--- 2. Enrolling Students in Courses ---")
    for course in [csc301, csc305, mth301]:
        aisha.enroll_course(course)
        musa.enroll_course(course)

    print(f"Aisha enrolled in {len(aisha.enrolled_courses)} courses ({aisha.total_credits} Credit Units).")
    print(f"Musa enrolled in {len(musa.enrolled_courses)} courses ({musa.total_credits} Credit Units).")

    # 5. Tracking Attendance
    print("\n--- 3. Simulating Semester Attendance ---")
    # Aisha: high attendance in CSC301 (10/10)
    for _ in range(10):
        aisha.attendance.mark_attendance("CSC301", is_present=True)
    # Aisha: 8/10 in CSC305
    for _ in range(8):
        aisha.attendance.mark_attendance("CSC305", is_present=True)
    for _ in range(2):
        aisha.attendance.mark_attendance("CSC305", is_present=False)

    print(aisha.attendance.get_summary_report())

    # 6. Lecturer Grading & Assessment Submission
    print("\n--- 4. Lecturers Submitting Assessment Scores ---")
    dr_kabir.submit_score(aisha, csc301, score=88.5)   # A (5 GP)
    dr_kabir.submit_score(aisha, csc305, score=74.0)   # A (5 GP)
    prof_amina.submit_score(aisha, mth301, score=68.0) # B (4 GP)

    dr_kabir.submit_score(musa, csc301, score=62.0)    # B (4 GP)
    dr_kabir.submit_score(musa, csc305, score=55.0)    # C (3 GP)
    prof_amina.submit_score(musa, mth301, score=72.0)  # A (5 GP)

    print("Scores submitted successfully by course lecturers.")

    # 7. Polymorphic Profile Cards
    print("\n--- 5. Polymorphic User Directory ---")
    users = [dr_kabir, prof_amina, aisha, musa]
    for u in users:
        print(u.display_profile())
        print("-" * 50)

    # 8. Generating Official Transcripts
    print("\n--- 6. Official Academic Transcripts ---")
    print(aisha.result.generate_transcript(aisha.name, aisha.matric_no, aisha.enrolled_courses))
    print("\n")
    print(musa.result.generate_transcript(musa.name, musa.matric_no, musa.enrolled_courses))


if __name__ == "__main__":
    main()
