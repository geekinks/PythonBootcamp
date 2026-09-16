# Exercise 05 — Encapsulation

**Difficulty**: 🟡 Intermediate

## Objective
Protect object invariants, use protected naming conventions (`_`), and prevent internal data tampering through encapsulation.

## Scenario
Implement a secure `GradeBook` class that records student scores for different courses, preventing invalid score entries and returning defensive copies of records.

## Requirements
1. Class `GradeBook`:
   - `__init__(self, student_id: str)`:
     - Store `student_id`.
     - Initialize a protected dictionary `_scores = {}`.
2. Method `record_score(self, course_code: str, score: float)`:
   - Validate that `score` is a numeric value (int or float).
   - Validate that `0.0 <= score <= 100.0`, raising `ValueError` otherwise.
   - Record the score in `_scores[course_code]`.
3. Method `get_score(self, course_code: str) -> float | None`:
   - Returns the score for `course_code` or `None` if not found.
4. Property `average_score -> float`:
   - Returns the arithmetic mean of all recorded scores, or `0.0` if empty.
5. Property `all_scores -> dict[str, float]`:
   - Returns a **defensive copy** of `_scores` so external callers cannot mutate internal records.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Encapsulation and data protection verified.
```
