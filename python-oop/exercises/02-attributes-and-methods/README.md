# Exercise 02 — Attributes and Methods

**Difficulty**: 🟢 Beginner

## Objective
Learn how to define instance attributes and behaviors (methods) using the `self` parameter.

## Scenario
Build a basic `Student` class that can record personal demographic data, register/drop courses, and display a profile card.

## Requirements
1. Define a class `Student`.
2. Implement a method `set_profile(self, name: str, matric_no: str, department: str, level: int)` that initializes instance attributes.
3. Initialize an empty list `courses` inside `set_profile`.
4. Implement `register_course(self, course_code: str)`:
   - Adds `course_code` to `self.courses` only if not already present.
5. Implement `drop_course(self, course_code: str)`:
   - Removes `course_code` if present.
6. Implement `get_profile_card(self) -> str` returning a formatted summary:
   `"Student: <name> | Matric: <matric_no> | Dept: <department> | Level: <level> | Courses: <count>"`

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Attributes and methods working properly.
```

## Hints
- Remember to use `self.` before every attribute name (e.g. `self.name`).
- Use list `.append()` and `.remove()`.
