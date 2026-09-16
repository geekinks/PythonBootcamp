# Assignment 04 — Learning Management System (LMS) Design Challenge

> **Comprehensive Architectural Design and Implementation**

## 1. Project Overview
Design and implement the core engine of an online Learning Management System (like Coursera, Udemy, or Canvas) supporting hierarchical course structures, auto-graded quizzes, peer assignments, and certificate generation upon completion.

---

## 2. Target Domain Entities

```text
LMS Domain Entities
├── User (Base)
│   ├── Student
│   └── Instructor
├── Course
├── Module / Section
├── Lesson (Abstract Content Unit)
│   ├── VideoLesson
│   ├── TextArticle
│   └── Quiz
├── QuizQuestion
├── Assignment
├── Enrollment
└── Certificate
```

---

## 3. Structural & Behavioral Specifications

### 3.1 Course Composition Hierarchy
- A `Course` has a title, instructor, and a list of `Module` objects.
- Each `Module` contains ordered `Lesson` instances.
- `Lesson` is an Abstract Base Class (`ABC`) with methods `get_duration()`, `complete(student: Student)`.
- `VideoLesson`, `TextArticle`, and `Quiz` inherit from `Lesson` with specialized content.

### 3.2 Quiz & Auto-Grading Engine
- A `Quiz` contains multiple `QuizQuestion` objects.
- Each question has a prompt, options, correct answer index, and point value.
- When a student submits an answer sheet, the quiz computes the percentage score and marks itself passed if score `>= passing_threshold` (e.g. 70%).

### 3.3 Enrollment & Progress Tracking
- An `Enrollment` associates a `Student` with a `Course`.
- Tracks completed lesson IDs.
- Provides a computed property `progress_percentage -> float`.

### 3.4 Certificate Issuance
- When `progress_percentage == 100.0`, the system automatically generates a unique `Certificate` with verification hash, completion date, and student name.

---

## 4. Deliverables
1. **Design Document (`design.md`)**:
   - Complete Mermaid class diagram showing all 8+ entities, relationships, and multiplicity.
   - Narrative explaining design choices, trade-offs, and adherence to SOLID principles.
2. **Python Implementation**:
   - Modular code in `src/`.
   - Executable simulation in `main.py` enrolling a student, completing lessons, passing a quiz, and receiving a certificate.
3. **Automated Unit Tests**:
   - Verification of progress calculations, quiz grading logic, and certificate issuance boundaries.
