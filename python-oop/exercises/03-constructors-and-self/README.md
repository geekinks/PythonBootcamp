# Exercise 03 — Constructors and Self

**Difficulty**: 🟢 Beginner

## Objective
Use `__init__` to initialize object state automatically upon instantiation and handle default parameters.

## Scenario
Convert the manual setup method into a robust `__init__` constructor for a `Course` and `Student` class so that invalid, uninitialized instances cannot be created.

## Requirements
1. Implement class `Course`:
   - `__init__(self, code: str, title: str, credit_units: int = 3)`
   - Stores `code`, `title`, and `credit_units`.
2. Implement class `Student`:
   - `__init__(self, name: str, matric_no: str, department: str, level: int = 100)`
   - Stores `name`, `matric_no`, `department`, and `level` (default 100).
   - Initializes `enrolled_courses` as an empty list.
   - Implement `enroll(self, course: Course)` to append course to `enrolled_courses` (prevent duplicates).
   - Implement `total_credits(self) -> int` that returns the sum of credit units for all enrolled courses.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Constructors and self implemented properly.
```
