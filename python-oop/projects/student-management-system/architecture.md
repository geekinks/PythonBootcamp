# Student Management System — Architecture Overview

> **Subsystems, Component Boundaries, and Data Flow**

---

## 1. System Architecture Layers

The Student Management System is organized into four modular layers:

```text
┌─────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                      │
│                main.py / CLI Interactive Runner             │
├─────────────────────────────────────────────────────────────┤
│                       DOMAIN SERVICES                       │
│     ResultProcessor (Strategy)  │  AttendanceTracker Engine │
├─────────────────────────────────────────────────────────────┤
│                        DOMAIN MODELS                        │
│   User <── Student, Lecturer  │  Course  │  Department      │
├─────────────────────────────────────────────────────────────┤
│                      PERSISTENCE / DATA                     │
│                In-Memory Models & Defensive State           │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Component Breakdown

### 2.1 Identity & User Subsystem (`src/user.py`, `src/student.py`, `src/lecturer.py`)
- Defines the core abstract/base identity contracts.
- Specializes roles into `Student` (course enrollment, transcripts, attendance) and `Lecturer` (course teaching, grade submissions).

### 2.2 Academic Catalog Subsystem (`src/course.py`)
- Models academic courses, credit units, and departmental containers.
- Decouples course catalog definitions from student enrollments.

### 2.3 Evaluation & Results Subsystem (`src/result.py`)
- Implements the Strategy Pattern via `ResultProcessor(ABC)`.
- `Standard5PointGPAProcessor` provides grading scales, quality point calculations, and academic honors determination.
- `Result` manages student score collections and transcript formatting.

### 2.4 Attendance Subsystem (`src/attendance.py`)
- Records per-course session attendance logs.
- Calculates attendance ratios and exam qualification flags.

---

## 3. Data Flow Diagram

```text
1. Department registers Course (CSC301, 3 Credits)
                     │
2. Lecturer assigned to Course (Dr. Kabir -> CSC301)
                     │
3. Student enrolls in Course (Aisha -> CSC301)
                     │
4. Attendance logged during semester (Aisha: 18/20 sessions = 90%)
                     │
5. Lecturer submits final assessment score (Dr. Kabir -> Aisha: 85%)
                     │
6. Result validates score & delegates to ResultProcessor (5 GP * 3 = 15 QP)
                     │
7. System generates Official Transcript & Academic Standing (GPA 5.00, First Class)
```
