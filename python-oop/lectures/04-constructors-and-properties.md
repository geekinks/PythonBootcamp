# Lecture 04 — Constructors and Properties

> **Automating Initialization and Creating Smart Attribute Interfaces**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Explain why manual initialization (like `obj.initialize(...)`) is fragile.
2. Use Python's special `__init__` constructor method to guarantee valid object creation.
3. Use default argument values and type hints in `__init__`.
4. Distinguish between simple attributes and `@property` getters/setters.
5. Create computed (read-only) properties and validated (writable) properties.
6. Design clean Pythonic interfaces that protect data without verbose Java-style getters.

---

## Prerequisites
- Completed [Lecture 03 — Attributes, Methods, and `self`](03-attributes-methods-and-self.md).

---

## 1. Introduction: The Need for Constructors

In Lecture 03, we created an empty object and manually called `student.initialize(...)`. But what happens if a programmer forgets to call `initialize()`?

```python
student = Student()
# Programmer forgets initialize()
student.display_profile() # CRASH! AttributeError: 'Student' object has no attribute 'name'
```

We need a way to ensure that **an object cannot exist in an uninitialized, invalid state**.

In Python, the **`__init__`** method (pronounced "dunder init", for double-underscore init) serves as the **constructor / initializer**. It is invoked **automatically** at the moment an object is instantiated.

---

## 2. Defining and Using `__init__`

```python
class Student:
    """Represents an enrolled student."""

    def __init__(self, name: str, matric_no: str, level: int = 100):
        """
        Initialize student instance attributes.
        :param name: Full name of student
        :param matric_no: Unique matriculation identifier
        :param level: Academic level (defaults to 100)
        """
        self.name = name
        self.matric_no = matric_no
        self.level = level
        self.courses = []

# Now, instantiation automatically calls __init__
s1 = Student("Aisha Muhammad", "GSU/CSC/001")        # uses default level=100
s2 = Student("Musa Bello", "GSU/CSC/002", level=300) # explicit level=300

print(f"{s1.name} (Level {s1.level})")
print(f"{s2.name} (Level {s2.level})")
```

Attempting `Student()` without arguments now raises a clear `TypeError: __init__() missing 2 required positional arguments: 'name' and 'matric_no'`. This protects the integrity of our program!

---

## 3. Stored Attributes vs Computed Properties

Consider a student with `first_name` and `last_name`. If we store `full_name` as a normal attribute:

```python
class BrokenStudent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"

s = BrokenStudent("Aisha", "Muhammad")
print(s.full_name) # "Aisha Muhammad"

# Now suppose Aisha changes her last name:
s.last_name = "Bello"
print(s.full_name) # Still "Aisha Muhammad"! Out of sync!
```

Storing redundant state causes **data synchronization bugs**.

### The Solution: `@property` (Computed Attributes)

The `@property` decorator turns a method into a read-only attribute that is dynamically calculated when accessed:

```python
class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        """Dynamically compute full name on demand."""
        return f"{self.first_name} {self.last_name}"

s = Student("Aisha", "Muhammad")
print(s.full_name) # Aisha Muhammad

s.last_name = "Bello"
print(s.full_name) # Aisha Bello (Always in sync!)
```

Notice we access `s.full_name` **without parentheses**, exactly like a standard attribute!

---

## 4. Controlled Attributes with Getters and Setters

What if we want an attribute that can be updated, but must adhere to strict validation rules (e.g., student level must be 100, 200, 300, 400, or 500)?

We pair `@property` with `@<attribute>.setter`:

```python
class Student:
    VALID_LEVELS = {100, 200, 300, 400, 500}

    def __init__(self, name: str, matric_no: str, level: int = 100):
        self.name = name
        self.matric_no = matric_no
        # Using the property setter inside __init__ guarantees validation!
        self.level = level

    @property
    def level(self) -> int:
        """Getter for level."""
        return self._level

    @level.setter
    def level(self, value: int):
        """Setter with validation."""
        if not isinstance(value, int):
            raise TypeError("Academic level must be an integer.")
        if value not in self.VALID_LEVELS:
            raise ValueError(f"Invalid level: {value}. Allowed: {sorted(self.VALID_LEVELS)}")
        self._level = value
```

### Testing the Validation:
```python
student = Student("Aisha", "GSU/CSC/001", 200)
print(student.level) # 200

student.level = 300  # Works! Valid update.
print(student.level) # 300

try:
    student.level = 999  # Throws ValueError!
except ValueError as e:
    print(f"Caught validation error: {e}")
```

---

## 5. Mental Model: Attribute vs Property

```text
Attribute
    ↓
Direct memory storage (e.g. self.name = "Aisha")
No computation or interception on read/write.

Property (@property)
    ↓
A method disguised as an attribute.
Interception on read (getter) and write (setter).
Used for:
  1. Computed values (e.g. full_name, gpa)
  2. Input validation (e.g. score >= 0 and <= 100)
  3. Read-only fields (provide getter without setter)
```

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> Why doesn't Python encourage writing Java-style methods like `get_level()` and `set_level()` everywhere by default?
> *Python's philosophy: Start with simple public attributes (`student.level`). If you later need validation or computed logic, seamlessly convert it to a `@property` without breaking existing external code that accesses `student.level`!*

### 💬 Discuss
> If a property has a `@property` getter but NO `@<name>.setter`, what happens if you try to execute `student.full_name = "New Name"`?

### 💻 Code Along: Read-Only Property
Run this to see how Python handles read-only properties:
```python
class ReadOnlyDemo:
    def __init__(self, code: str):
        self._code = code

    @property
    def code(self):
        return self._code

demo = ReadOnlyDemo("CSC301")
print(demo.code)
try:
    demo.code = "CSC999" # Cannot set attribute!
except AttributeError as err:
    print(f"Expected Error: {err}")
```

### 🔍 Debug This
Why does this code cause an infinite recursion `RecursionError`?

```python
class BrokenSetter:
    def __init__(self, score: float):
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        # BUG: self.score = value calls the setter again recursively!
        # Should be self._score = value
        self.score = value
```

---

## 7. Knowledge Check & Quiz

1. **When is the `__init__` method called?**
   - A) Only when the script terminates
   - B) Automatically when a new instance of the class is created
   - C) Whenever an attribute is deleted
   - D) Manually by calling `student.__init__()`
   *(Answer: B)*

2. **What decorator is used to define a getter method that acts like an attribute?**
   - A) `@getter`
   - B) `@classmethod`
   - C) `@property`
   - D) `@attribute`
   *(Answer: C)*

3. **To make a property `gpa` read-only, what should you do?**
   - A) Define only `@property def gpa(self):` without a `@gpa.setter`
   - B) Mark the class as `final`
   - C) Delete the `__init__` method
   - D) Use `global gpa`
   *(Answer: A)*

---

## 8. Common Mistakes
- **Returning values from `__init__`**: `__init__` must always return `None`. Writing `return self` or `return "Success"` raises a `TypeError`.
- **Infinite recursion in setters**: Writing `self.val = val` inside `val.setter` instead of `self._val = val`.
- **Calling properties with parentheses**: Writing `student.full_name()` when `@property` was used causes `TypeError: 'str' object is not callable`.

---

## 9. Key Takeaways
- Use `__init__` to guarantee every object starts in a consistent, valid initial state.
- Use default parameters in `__init__` for optional configuration.
- Use `@property` for computed values to eliminate stale state synchronization bugs.
- Use `@property` + `@property.setter` for transparent validation without cluttering code with `get_x()` and `set_x()` boilerplate.

---

## 10. Homework & Exercises
- Complete [Exercise 03 — Constructors and Self](../exercises/03-constructors-and-self/README.md).
- Complete [Exercise 04 — Properties](../exercises/04-properties/README.md).
- Read [Lecture 05 — Encapsulation](05-encapsulation.md).
