# Exercise 10 — OOP Design & Class Methods

**Difficulty**: 🔴 Challenge

## Objective
Implement factory constructors (`@classmethod`), utility validation methods (`@staticmethod`), and shared class state tracking.

## Scenario
Build a production-grade `StudentEnrollment` factory that parses varied data feeds (JSON / Dict and Delimited CSV rows), automatically generates sequential matriculation numbers, and tracks total system matriculation counters.

## Requirements
1. Class `Student`:
   - Class attribute `_enrollment_counter = 0`
   - Class attribute `TOTAL_CAPACITY = 1000`
   - `__init__(self, name: str, email: str, matric_no: str, level: int)`
2. Factory Method `@classmethod from_csv(cls, csv_string: str) -> Student`:
   - Parses `"Name, Email, Level"` and auto-generates matric number using `cls._generate_matric_no()`.
3. Factory Method `@classmethod from_dict(cls, payload: dict) -> Student`:
   - Parses dictionary keys `{"name": "...", "email": "...", "level": ...}` and auto-generates matric number.
4. Helper Method `@classmethod _generate_matric_no(cls) -> str`:
   - Increments `cls._enrollment_counter` and returns `f"GSU/CSC/{cls._enrollment_counter:04d}"` (e.g. `GSU/CSC/0001`).
5. Static Method `@staticmethod validate_email(email: str) -> bool`:
   - Returns `True` if email contains `@` and `.edu` or `.com`.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Class and static methods operating correctly.
```
