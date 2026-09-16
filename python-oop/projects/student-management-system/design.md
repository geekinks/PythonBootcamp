# Student Management System — Detailed Domain Design

> **Class Blueprints, Design Decisions, Invariant Rules, and UML Diagrams**

---

## 1. Domain Model Class Diagram

```mermaid
classDiagram
    direction TB

    class User {
        <<abstract>>
        #str _name
        #str _email
        #str _user_id
        +name str
        +email str
        +user_id str
        +display_profile()* str
        +send_notification(message: str) str
    }

    class Student {
        -str _matric_no
        -int _level
        -List~Course~ _enrolled_courses
        +Result result
        +AttendanceTracker attendance
        +matric_no str
        +level int
        +enrolled_courses List~Course~
        +enroll_course(course: Course) bool
        +drop_course(course_code: str) bool
        +total_credits int
        +display_profile() str
    }

    class Lecturer {
        -str _staff_id
        -str _department_name
        -List~Course~ _assigned_courses
        +staff_id str
        +department_name str
        +assigned_courses List~Course~
        +assign_course(course: Course) bool
        +submit_score(student: Student, course: Course, score: float) bool
        +display_profile() str
    }

    class Course {
        -str _code
        -str _title
        -int _credit_units
        +code str
        +title str
        +credit_units int
        +display_info() str
    }

    class Department {
        -str _name
        -str _code
        -List~Course~ _courses
        -List~Lecturer~ _faculty
        -List~Student~ _students
        +add_course(course: Course)
        +add_faculty(lecturer: Lecturer)
        +add_student(student: Student)
        +get_summary() str
    }

    class ResultProcessor {
        <<interface>>
        +score_to_grade_point(score: float)* int
        +score_to_letter_grade(score: float)* str
        +calculate_gpa(scores: dict, courses: list)* float
        +determine_standing(gpa: float)* str
    }

    class Standard5PointGPAProcessor {
        +score_to_grade_point(score: float) int
        +score_to_letter_grade(score: float) str
        +calculate_gpa(scores: dict, courses: list) float
        +determine_standing(gpa: float) str
    }

    class Result {
        -dict _scores
        +ResultProcessor processor
        +add_score(course_code: str, score: float)
        +get_score(course_code: str) float
        +all_scores dict
        +calculate_gpa(courses: list) float
        +generate_transcript(student_name: str, courses: list) str
    }

    class AttendanceTracker {
        -dict _records
        +mark_attendance(course_code: str, present: bool)
        +get_course_attendance(course_code: str) dict
        +is_eligible_for_exam(course_code: str, threshold: float) bool
    }

    User <|-- Student : Inheritance (IS-A)
    User <|-- Lecturer : Inheritance (IS-A)
    ResultProcessor <|.. Standard5PointGPAProcessor : Implements Contract
    
    Student *-- Result : Composition (Strictly Owns)
    Student *-- AttendanceTracker : Composition (Strictly Owns)
    Student o-- Course : Aggregation (References)
    
    Lecturer o-- Course : Association (Teaches)
    Department o-- Course : Aggregation
    Department o-- Lecturer : Aggregation
    Department o-- Student : Aggregation
    Result --> ResultProcessor : Strategy (DIP)
```

---

## 2. Key Design Decisions & Trade-Offs

### 2.1 Why Composition for `Result` and `AttendanceTracker`?
- A `Student` is neither a `Result` nor an `AttendanceTracker` (violating `IS-A`).
- By composing these components into `Student`, we keep the `Student` class clean and focused on identity and course tracking (SRP), delegating grading algorithms and attendance logs to specialized domain objects.

### 2.2 Why Dependency Inversion on `ResultProcessor`?
- Different universities and educational systems use different grading scales (e.g. 5.0 scale in Nigeria, 4.0 scale in USA, percentage in UK, 10-point scale in India).
- By injecting `ResultProcessor` into `Result`, we can swap grading standards at runtime without changing a single line in `Student` or `Result` (Open/Closed Principle).

### 2.3 Protection of Internal Invariants
- `_scores` and `_records` dictionaries are encapsulated with private/protected naming and exposed only via copy methods, preventing external code from corrupting internal grades or attendance numbers.
