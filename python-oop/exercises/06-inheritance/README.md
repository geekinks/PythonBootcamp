# Exercise 06 — Inheritance

**Difficulty**: 🟡 Intermediate

## Objective
Establish a clean class hierarchy with a parent class `User` and child classes `Student` and `Lecturer`, utilizing `super()` and method overriding.

## Scenario
Model institutional users. Both students and lecturers have names, emails, and roles, but students hold matric numbers while lecturers hold staff IDs and departmental assignments.

## Requirements
1. Base Class `User`:
   - `__init__(self, name: str, email: str)`
   - Method `get_role(self) -> str` returning `"User"`
   - Method `format_header(self) -> str` returning `f"[{self.get_role()}] {self.name} <{self.email}>"`
2. Subclass `Student(User)`:
   - `__init__(self, name: str, email: str, matric_no: str, level: int = 100)` -> calls `super().__init__(name, email)`
   - Override `get_role(self) -> str` to return `"Student"`
3. Subclass `Lecturer(User)`:
   - `__init__(self, name: str, email: str, staff_id: str, department: str)` -> calls `super().__init__(name, email)`
   - Override `get_role(self) -> str` to return `"Lecturer"`

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Inheritance hierarchy functioning as expected.
```
