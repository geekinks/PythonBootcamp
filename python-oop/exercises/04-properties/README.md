# Exercise 04 — Properties

**Difficulty**: 🟡 Intermediate

## Objective
Implement computed properties (`@property`) and validated properties (`@setter`) to protect object state without broken synchronization.

## Scenario
Create a `StudentProfile` class that maintains `first_name`, `last_name`, `email`, and `cgpa`.

## Requirements
1. Implement class `StudentProfile`:
   - `__init__(self, first_name: str, last_name: str, email: str, cgpa: float = 0.0)`
2. Computed Property `full_name`:
   - Returns `f"{first_name} {last_name}"`.
   - Setter for `full_name`: If assigned a string (e.g. `"Fatima Bello"`), splits into `first_name` and `last_name`.
3. Validated Property `cgpa`:
   - Getter returns the float `_cgpa`.
   - Setter checks that `0.0 <= value <= 5.0`. If out of bounds, raises `ValueError("CGPA must be between 0.0 and 5.0")`.
4. Read-Only Property `academic_standing`:
   - Returns `"First Class"` if `cgpa >= 4.50`
   - Returns `"Second Class Upper"` if `3.50 <= cgpa < 4.50`
   - Returns `"Second Class Lower"` if `2.40 <= cgpa < 3.50`
   - Returns `"Third Class"` if `1.50 <= cgpa < 2.40`
   - Returns `"Probation"` if `cgpa < 1.50`

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Properties and setters work correctly.
```
