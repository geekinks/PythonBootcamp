# Lecture 01 — Python & OOP Introduction

> **From Scripts to Systems: Why Object-Oriented Programming Matters**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Explain what Python is and why it supports multiple programming paradigms.
2. Contrast procedural, functional, and object-oriented programming with practical examples.
3. Identify the failure points of large-scale procedural systems (state sprawl, tight coupling, code duplication).
4. Explain how OOP helps model real-world domains by encapsulating state and behavior.
5. Understand the mental shift: **Don't just write classes — learn to model problems**.

---

## Prerequisites
- Basic familiarity with Python syntax (variables, data types, `if`/`else`, `for` loops, functions, lists, dictionaries).

---

## 1. Introduction: What is Python?
Python is a high-level, interpreted, dynamically typed, and multi-paradigm programming language. Being **multi-paradigm** means Python does not force you into a single style of thinking. You can choose the paradigm that best fits the problem at hand:

```text
                         PYTHON
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
     Procedural            OOP          Functional
          │                 │                 │
     Procedures          Objects          Functions
     Functions           Classes          Transformations
     Step-by-step        State + Logic    Pure pipelines
```

---

## 2. The Three Core Paradigms Compared

### 2.1 Procedural Programming
Focuses on a sequence of actions or procedure calls operating on separate data structures.

```python
# Procedural approach to calculating student averages
student_name = "Aisha"
scores = [85, 90, 78]

def calculate_average(score_list):
    return sum(score_list) / len(score_list)

print(f"{student_name}'s average: {calculate_average(scores):.2f}")
```
- **When to use**: Quick automation scripts, simple data analysis, linear algorithmic pipelines, file conversions.

### 2.2 Functional Programming
Focuses on pure functions, immutability, and data transformations without side effects.

```python
# Functional approach using map and lambda
scores = [85, 90, 78]
letter_grades = list(map(lambda s: 'A' if s >= 70 else 'B', scores))
print(letter_grades)
```
- **When to use**: Data filtering/mapping pipelines, concurrent processing, ETL workflows.

### 2.3 Object-Oriented Programming (OOP)
Focuses on bundling data (**state**) and functions that operate on that data (**behavior**) into cohesive units called **objects**.

```python
class Student:
    def __init__(self, name: str, scores: list[float]):
        self.name = name
        self.scores = scores

    def calculate_average(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

student = Student("Aisha", [85, 90, 78])
print(f"{student.name}'s average: {student.calculate_average():.2f}")
```
- **When to use**: Complex domain models (Student Management, Banking, E-commerce, Game engines), systems with evolving entities and business rules.

---

## 3. Real-World Analogy: The University Registry Office

Imagine a university registry office where all student records are loose papers scattered on a giant shared desk:
- Any staff member can walk by and modify any paper without validation.
- If a student changes their department, five different binders across three offices must be manually updated in sync.
- If one binder format changes, every staff member's workflow breaks.

**This is the procedural disaster:** Global state, lack of boundaries, and procedures scattered across code files.

**The OOP solution:**
Each student has a dedicated, secure digital record container. Only authorized operations can update courses, calculate GPAs, or record attendance. The data and the rules governing that data live in one place.

---

## 4. The Problem with Large Procedural Systems

Let's look at how a procedural Student Management System inevitably degrades as requirements grow.

### The Procedural Way:
```python
# procedural_sms.py
students = [
    {"name": "Aisha", "matric": "GSU/CSC/001", "scores": {"CSC301": 85}},
    {"name": "Muhammad", "matric": "GSU/CSC/002", "scores": {"CSC301": 92}}
]

def add_score(student_matric, course_code, score):
    # What if someone passes score = -50 or score = 999?
    # What if student_matric does not exist?
    # What if scores dict is missing?
    for s in students:
        if s["matric"] == student_matric:
            s["scores"][course_code] = score
            return True
    return False

def print_transcript(student_matric):
    for s in students:
        if s["matric"] == student_matric:
            total = sum(s["scores"].values())
            avg = total / len(s["scores"]) if s["scores"] else 0
            print(f"Student: {s['name']} | Average: {avg:.1f}")
```

### Why this breaks at scale:
1. **Data Fragility**: Any function anywhere in the codebase can do `student["scores"] = "INVALID"` or modify keys without validation.
2. **Duplication of Validation**: Every function interacting with `students` must re-implement checks.
3. **No Invariants**: There is no single authority ensuring business rules (e.g., score between 0 and 100).
4. **Maintenance Nightmare**: If you rename `"matric"` to `"matric_no"`, dozens of functions crash across the system.

---

## 5. The OOP Mental Model: Modeling the Domain

The core philosophy of this course is:

```text
Problem
   ↓
Entities
   ↓
Data (State)
   ↓
Behavior (Methods)
   ↓
Responsibilities
   ↓
Relationships
   ↓
Classes & Objects
   ↓
Working System
```

Instead of asking *"What functions do I need to write?"*, ask:
1. **What entities exist in the real world?** (`Student`, `Lecturer`, `Course`, `Result`, `Department`)
2. **What does each entity know?** (Attributes: `name`, `matric_no`, `credit_units`)
3. **What can each entity do or have done to it?** (Methods: `register_course()`, `submit_score()`, `compute_gpa()`)
4. **How do these entities collaborate?** (Relationships: Lecturer *teaches* Course, Student *enrolls in* Course)

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> Why do we not use OOP for a 10-line script that renames 500 JPEG files in a folder?
> *Hint: Overhead vs. domain complexity.*

### 💬 Discuss
> In pairs or groups, list 3 entities in an ATM banking system and identify 2 pieces of data and 2 behaviors for each.

### 💻 Code Along
Open a Python REPL or terminal and run this comparison:

```python
# Procedural Dictionary
dict_student = {"name": "Fatima", "level": 200}
dict_student["level"] = -999  # Nothing prevents this nonsense!

# OOP Class with boundary
class SafeStudent:
    def __init__(self, name: str, level: int):
        self.name = name
        self.set_level(level)

    def set_level(self, level: int):
        if level not in [100, 200, 300, 400, 500]:
            raise ValueError(f"Invalid university level: {level}")
        self.level = level

safe = SafeStudent("Fatima", 200)
# safe.set_level(-999) # Raises ValueError immediately!
print(f"Safe student initialized: {safe.name}, Level: {safe.level}")
```

### 🔍 Debug This
Look at the following broken procedural code. What goes wrong when a new student without scores is added?

```python
students = [
    {"name": "Zainab", "scores": []},
    {"name": "Ali", "scores": [70, 80]}
]

for s in students:
    # BUG: ZeroDivisionError when scores is empty!
    avg = sum(s["scores"]) / len(s["scores"])
    print(s["name"], avg)
```

---

## 7. Knowledge Check & Quiz

1. **Which programming paradigm is focused primarily on step-by-step procedures over shared state?**
   - A) Functional
   - B) Procedural
   - C) Object-Oriented
   - D) Declarative
   *(Answer: B)*

2. **True or False:** OOP should be used for every single Python script, regardless of size or complexity.
   *(Answer: False — simple scripts are often cleanest written procedurally).*

3. **In OOP terminology, bundling data and the methods that operate on that data is called:**
   - A) Recursion
   - B) Encapsulation
   - C) Iteration
   - D) Compilation
   *(Answer: B)*

---

## 8. Common Mistakes
- **Over-engineering simple tasks**: Creating a 6-class hierarchy just to parse a single CSV file.
- **Treating classes as just dictionaries**: Writing classes with only public fields and writing all logic outside in helper functions.
- **Ignoring domain modeling**: Starting to code classes before identifying what entities and boundaries actually exist.

---

## 9. Key Takeaways
- Python is multi-paradigm: use Procedural for scripts/algorithms, Functional for data pipelines, and OOP for modeling complex real-world domains.
- Procedural code struggles as systems scale due to loose data integrity and scattered logic.
- OOP bundles state and behavior together, making code modular, maintainable, and robust.
- **Rule of thumb**: Don't just write classes; model problems and protect invariants.

---

## 10. Homework
1. Write down on paper a list of entities, data, and actions needed for a **Hospital Management System** (Doctors, Patients, Appointments).
2. Read [Lecture 02 — Classes and Objects](02-classes-and-objects.md).
