# Exercise 01 — Classes and Objects

**Difficulty**: 🟢 Beginner

## Objective
Learn how to define custom class blueprints in Python and instantiate multiple distinct objects.

## Scenario
The Geekink Institute is digitizing its department registry. You need to define blueprints for `Student`, `Lecturer`, and `Course`, instantiate specific objects for each, and verify their identities.

## Requirements
1. Define three empty classes: `Student`, `Lecturer`, and `Course`.
2. Instantiate two student objects: `student1` and `student2`.
3. Instantiate one lecturer object: `lecturer1`.
4. Instantiate one course object: `course1`.
5. Demonstrate that `student1` and `student2` are separate objects in memory (`student1 is not student2`).
6. Verify their types using `isinstance()`.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
When running `python3 starter.py`, all verification assertions should pass with output:
```text
All tests passed successfully! Classes and objects created correctly.
```

## Hints
- Use the `pass` keyword inside an empty class body.
- Instantiation syntax is `Classname()`.
- The `is` keyword compares object identity (memory addresses).

## Extension Challenge
Create a list containing all 4 instantiated objects and write a loop that prints the class name of each object using `type(obj).__name__`.
