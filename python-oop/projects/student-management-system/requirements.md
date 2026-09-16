# Student Management System — Requirements Specification

> **Functional and Non-Functional Requirements for Academic Management Engine**

---

## 1. Project Overview
The **Student Management System (SMS)** is an object-oriented Python application designed to model and automate core academic operations in higher education institutions: student admissions, departmental course cataloging, lecturer course assignments, assessment scoring, GPA calculation, and attendance tracking.

---

## 2. Functional Requirements (FR)

### FR-01: User & Identity Management
- **FR-01.1**: The system shall provide a base `User` entity encapsulating common personal attributes: full name, email address, and system identifier.
- **FR-01.2**: Specialized user roles (`Student`, `Lecturer`) must inherit from `User` and provide specialized profile representations.
- **FR-01.3**: The system must validate email formats upon user creation.

### FR-02: Course & Department Catalog
- **FR-02.1**: The system shall model academic `Course` instances with course code, title, and credit units (positive integers between 1 and 6).
- **FR-02.2**: The system shall model `Department` instances that group related courses, enrolled students, and teaching faculty.
- **FR-02.3**: Courses shall support formatting descriptive course catalog cards.

### FR-03: Student Enrollment & Academic Progression
- **FR-03.1**: Students shall be able to enroll in courses offered by departments.
- **FR-03.2**: Duplicate course registrations by the same student shall be prevented.
- **FR-03.3**: Students shall be able to drop enrolled courses.
- **FR-03.4**: Students shall track academic levels (100, 200, 300, 400, 500) and support promotion to subsequent levels.

### FR-04: Lecturer & Teaching Assignment
- **FR-04.1**: Lecturers shall be assigned to teach one or more active courses.
- **FR-04.2**: Lecturers shall have the authority to submit assessment scores for students enrolled in their assigned courses.

### FR-05: Assessment, Grading & GPA Computation
- **FR-05.1**: Scores recorded for any course must be strictly validated within the numeric range `0.0 <= score <= 100.0`.
- **FR-05.2**: The system shall calculate Grade Point Averages (GPA) using an extensible, pluggable `ResultProcessor` strategy (defaulting to the Nigerian / US 5.0 scale).
- **FR-05.3**: The system shall classify academic standings (First Class, Second Class Upper, Second Class Lower, Third Class, Pass, Probation) based on computed GPA.
- **FR-05.4**: The system shall generate comprehensive academic transcripts detailing individual course scores, letter grades, quality points, and overall GPA.

### FR-06: Attendance Tracking
- **FR-06.1**: The system shall track student attendance per course session.
- **FR-06.2**: The system shall compute individual course attendance percentages.
- **FR-06.3**: The system shall determine exam eligibility based on minimum attendance threshold (e.g. >= 75%).

---

## 3. Non-Functional Requirements (NFR)

### NFR-01: Object-Oriented Integrity & Invariant Protection
- All class attributes with business constraints must be encapsulated using protected variables (`_attr`) and property getters/setters.
- Internal collections (e.g. score dictionaries, course lists) must return defensive copies to avoid external mutation leaks.

### NFR-02: Extensibility (SOLID Compliance)
- Grading rules, notification senders, and user types must follow the Open/Closed Principle (OCP) using Abstract Base Classes (`ABC`).

### NFR-03: Code Quality & Style
- Strict adherence to PEP 8 standards, descriptive naming conventions, explicit type hinting (`typing`), and comprehensive docstrings across all public methods.

### NFR-04: Testability & Reliability
- 100% test coverage for core business invariants: score bounds, duplicate enrollment prevention, GPA calculations, and inheritance polymorphism.
