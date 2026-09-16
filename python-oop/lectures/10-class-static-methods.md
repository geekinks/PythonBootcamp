# Lecture 10 — Class Methods and Static Methods

> **Instance vs Class vs Static: Understanding the 3 Method Types in Python**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Compare the 3 method types in Python: Instance methods, Class methods (`@classmethod`), and Static methods (`@staticmethod`).
2. Explain the purpose of `self` (current instance) vs `cls` (current class).
3. Use class attributes to maintain shared state (e.g. total enrolled students, matriculation counter).
4. Implement **Factory Methods** using `@classmethod` (e.g. creating students from JSON or CSV strings).
5. Implement pure utility functions using `@staticmethod`.

---

## Prerequisites
- Completed [Lecture 04 — Constructors and Properties](04-constructors-and-properties.md).

---

## 1. The Three Method Types at a Glance

In Python, methods inside a class can operate at three different levels of scope:

| Method Type | Decorator | First Parameter | Access Scope | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Instance Method** | None (default) | `self` | Instance attributes + Class attributes | Modifying or accessing individual object state. |
| **Class Method** | `@classmethod` | `cls` | Class attributes only (no `self`) | Factory constructors, class-wide state management. |
| **Static Method** | `@staticmethod` | None | No access to `self` or `cls` | Isolated utility/helper functions related to the domain. |

```text
┌─────────────────────────────────────────────────────────────┐
│                        class Student                        │
│                                                             │
│  [CLASS STATE]                                              │
│  total_students = 0                                         │
│                                                             │
│  [CLASS METHOD]                                             │
│  @classmethod from_csv(cls, data_string) -> cls(...)        │
│                                                             │
│  [STATIC METHOD]                                            │
│  @staticmethod is_valid_matric_format(matric) -> bool        │
│                                                             │
│  [INSTANCE METHODS]                                         │
│  def __init__(self, name)                                   │
│  def display_profile(self)                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Class Attributes vs Instance Attributes

A **Class Attribute** is shared across all instances of that class.
An **Instance Attribute** belongs exclusively to a single instance.

```python
class Student:
    # Class attribute (shared by all students)
    institution_name = "Geekink Institute of Technology"
    total_enrolled = 0

    def __init__(self, name: str, matric_no: str):
        # Instance attributes (unique to each student)
        self.name = name
        self.matric_no = matric_no
        
        # Increment shared class counter
        Student.total_enrolled += 1

s1 = Student("Aisha", "GSU/001")
s2 = Student("Musa", "GSU/002")

print(s1.institution_name)    # Geekink Institute of Technology
print(s2.institution_name)    # Geekink Institute of Technology
print(Student.total_enrolled) # 2
```

---

## 3. Class Methods (`@classmethod`) and Alternative Constructors

A `@classmethod` receives the class object itself (`cls`) as its first argument, allowing it to instantiate new objects dynamically.

This is widely used for **Factory Methods** (alternative constructors):

```python
class Student:
    def __init__(self, name: str, email: str, matric_no: str, level: int):
        self.name = name
        self.email = email
        self.matric_no = matric_no
        self.level = level

    @classmethod
    def from_csv_line(cls, csv_line: str):
        """Factory constructor: create a Student from a comma-separated string."""
        parts = [p.strip() for p in csv_line.split(",")]
        name, email, matric_no, level_str = parts
        return cls(name, email, matric_no, int(level_str))

    @classmethod
    def from_dict(cls, data: dict):
        """Factory constructor: create a Student from a dictionary."""
        return cls(
            name=data["name"],
            email=data["email"],
            matric_no=data["matric_no"],
            level=int(data.get("level", 100))
        )
```

### Using Factory Methods:
```python
# Standard constructor
s1 = Student("Aisha", "aisha@uni.edu", "GSU/001", 300)

# Created from CSV record
s2 = Student.from_csv_line("Musa Bello, musa@uni.edu, GSU/002, 200")

# Created from JSON/Dict API payload
s3 = Student.from_dict({"name": "Zainab Ali", "email": "zainab@uni.edu", "matric_no": "GSU/003", "level": 100})

print(f"Loaded: {s1.name}, {s2.name}, {s3.name}")
```

---

## 4. Static Methods (`@staticmethod`)

A `@staticmethod` is essentially a regular function that is bound inside a class's namespace for logical grouping. It does not receive `self` or `cls`.

```python
import re

class Student:
    def __init__(self, name: str, matric_no: str):
        if not self.is_valid_matric_no(matric_no):
            raise ValueError(f"Invalid matric number format: {matric_no}")
        self.name = name
        self.matric_no = matric_no

    @staticmethod
    def is_valid_matric_no(matric_no: str) -> bool:
        """Utility: check if matric number matches format GSU/XXX/NNN."""
        pattern = r"^[A-Z]{3}/[A-Z]{3}/\d{3,4}$"
        return bool(re.match(pattern, matric_no))

    @staticmethod
    def calculate_letter_grade(score: float) -> str:
        """Utility: pure score-to-letter grade conversion."""
        if score >= 70: return "A"
        if score >= 60: return "B"
        if score >= 50: return "C"
        if score >= 45: return "D"
        if score >= 40: return "E"
        return "F"
```

### Using Static Methods:
```python
# Can be called on the class directly without creating an object!
print(Student.is_valid_matric_no("GSU/CSC/001"))  # True
print(Student.is_valid_matric_no("INVALID-123"))   # False
print(Student.calculate_letter_grade(88.5))         # A
```

---

## 5. Summary Comparison

```python
class MethodComparison:
    class_var = "Shared State"

    def __init__(self, inst_var):
        self.inst_var = inst_var

    # 1. Instance Method: knows about instance AND class
    def instance_method(self):
        return f"Instance: {self.inst_var}, Class: {self.class_var}"

    # 2. Class Method: knows ONLY about class
    @classmethod
    def class_method(cls):
        return f"Class only: {cls.class_var}"

    # 3. Static Method: knows about NEITHER
    @staticmethod
    def static_method(x, y):
        return x + y
```

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> Why should you use `cls(...)` inside a `@classmethod` constructor instead of explicitly hardcoding `Student(...)`?
> *If a child class `class InternationalStudent(Student):` inherits the class method, `cls(...)` will instantiate an `InternationalStudent` instance rather than forcing a `Student` instance!*

### 💬 Discuss
> If a method doesn't use `self` or `cls`, why put it inside the class as a `@staticmethod` instead of a top-level module function?
> *Namespace organization! Keeping helper functions inside the class groups related domain logic together (e.g. `Student.is_valid_matric_no`).*

### 💻 Code Along: Auto-Generating Matric Numbers
```python
class AutoStudent:
    _counter = 100

    def __init__(self, name: str):
        self.name = name
        self.matric_no = self._generate_matric()

    @classmethod
    def _generate_matric(cls) -> str:
        cls._counter += 1
        return f"GSU/CSC/{cls._counter}"

s1 = AutoStudent("Aisha")
s2 = AutoStudent("Bello")
print(s1.name, s1.matric_no) # Aisha GSU/CSC/101
print(s2.name, s2.matric_no) # Bello GSU/CSC/102
```

### 🔍 Debug This
Find the error in this factory method:

```python
class Course:
    def __init__(self, code: str, title: str):
        self.code = code
        self.title = title

    # BUG: Missing @classmethod decorator!
    def create_intro(cls, code):
        return cls(code, "Introduction to " + code)

c = Course.create_intro("CSC101") # TypeError: create_intro() missing 1 required positional argument: 'code'
```

---

## 7. Knowledge Check & Quiz

1. **What parameter is automatically passed to a `@classmethod`?**
   - A) `self` (the instance)
   - B) `cls` (the class object)
   - C) `super`
   - D) `None`
   *(Answer: B)*

2. **Which method type does NOT have access to either the instance (`self`) or the class (`cls`)?**
   - A) Instance method
   - B) Class method
   - C) Static method
   - D) Abstract method
   *(Answer: C)*

3. **What is a common real-world use case for `@classmethod`?**
   - A) Calculating a math formula
   - B) Alternative factory constructors (e.g., parsing JSON/CSV/Dict into an object)
   - C) Printing a string
   - D) Modifying private instance attributes
   *(Answer: B)*

---

## 8. Common Mistakes
- **Forgetting `@classmethod` or `@staticmethod` decorators**: Python will treat them as standard instance methods and try to pass `self`.
- **Modifying class attributes via `self`**: Writing `self.total_students += 1` creates a shadowed *instance* attribute on `self` rather than updating the shared *class* attribute! Always use `Student.total_students += 1` or `cls.total_students += 1`.
- **Hardcoding class name inside classmethod**: Always use `cls(...)` instead of `ClassName(...)` to support inheritance.

---

## 9. Key Takeaways
- **Instance methods** receive `self` and operate on specific object instances.
- **Class methods** (`@classmethod`) receive `cls` and operate on class state or act as alternative constructors.
- **Static methods** (`@staticmethod`) are self-contained utilities grouped within a class for clean namespacing.
- Modify shared class variables using `cls.var` or `ClassName.var`, not `self.var`.

---

## 10. Homework & Exercises
- Complete [Exercise 10 — OOP Design](../exercises/10-oop-design/README.md).
- Read [Lecture 11 — OOP Design Principles](11-oop-design-principles.md).
