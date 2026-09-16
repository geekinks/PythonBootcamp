# Exercise 08 — Abstraction

**Difficulty**: 🔴 Challenge

## Objective
Define an Abstract Base Class (ABC) with `@abstractmethod` to enforce contracts for grading engines.

## Scenario
The university needs a extensible evaluation subsystem. Different programs (Undergraduate 5.0 scale, Masters Percentage scale) compute academic standing differently, but must conform to the exact same contract.

## Requirements
1. Define Abstract Base Class `GradeCalculator(ABC)`:
   - `@abstractmethod def calculate_gpa(self, scores: list[float]) -> float`: abstract method.
   - `@abstractmethod def get_standing(self, gpa: float) -> str`: abstract method.
   - Concrete method `format_report(self, student_name: str, scores: list[float]) -> str`:
     - Calls `self.calculate_gpa(scores)` and `self.get_standing(gpa)` and returns:
       `"Report for <name>: GPA=<gpa:.2f> | Status=<standing>"`
2. Implement Concrete Subclass `Undergraduate5PointCalculator(GradeCalculator)`:
   - `calculate_gpa`: Map score (>=70: 5, >=60: 4, >=50: 3, >=45: 2, >=40: 1, else: 0). Return average grade point.
   - `get_standing`: If GPA >= 4.5 -> `"First Class"`, >= 3.5 -> `"Second Class Upper"`, >= 2.4 -> `"Second Class Lower"`, else -> `"Pass/Probation"`.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Abstract base classes and concrete implementations verified.
```
