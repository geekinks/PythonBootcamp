# Exercise 09 — Composition

**Difficulty**: 🔴 Challenge

## Objective
Model complex domain entities using **Object Composition** (HAS-A) and delegation rather than bloated inheritance trees.

## Scenario
Model a university `Department` that aggregates `Course` and `Student` objects, and a `Student` that is composed of a dedicated `Transcript` object.

## Requirements
1. Class `Course`:
   - `__init__(self, code: str, title: str, credit_units: int)`
2. Class `Transcript`:
   - `__init__(self)`: initializes an empty dict `_course_grades = {}` (maps `course_code -> score`)
   - `add_grade(self, course_code: str, score: float)`: validates `0 <= score <= 100` and saves.
   - `get_gpa(self) -> float`: calculates average score.
3. Class `Student`:
   - `__init__(self, name: str, matric_no: str)`: initializes name, matric_no, and creates a fresh `Transcript()` instance stored in `self.transcript`.
   - Method `record_score(self, course_code: str, score: float)`: delegates directly to `self.transcript.add_grade(...)`.
4. Class `Department`:
   - `__init__(self, name: str)`: initializes empty `students = []` and `courses = []`.
   - `add_student(self, student: Student)`: appends student.
   - `add_course(self, course: Course)`: appends course.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Composition and aggregation relationships working cleanly.
```
