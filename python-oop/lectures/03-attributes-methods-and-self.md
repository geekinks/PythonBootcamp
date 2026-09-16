# Lecture 03 — Attributes, Methods, and `self`

> **State and Behavior: Giving Life to Objects**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Distinguish between object **state** (attributes) and object **behavior** (methods).
2. Understand what the `self` parameter represents and why Python requires it.
3. Define instance attributes inside methods.
4. Define instance methods and invoke them on objects.
5. Contrast how Python translates `object.method(arg)` into `Class.method(object, arg)`.
6. Avoid the most common beginner pitfalls around `self` and instance data.

---

## Prerequisites
- Completed [Lecture 02 — Classes and Objects](02-classes-and-objects.md).

---

## 1. Introduction: State vs. Behavior

An object in OOP is a bundle of two things:
1. **Attributes (State / Data)**: What the object *knows* or *holds* (e.g., student name, matric number, level).
2. **Methods (Behavior / Actions)**: What the object *can do* or what can be done to it (e.g., register a course, display profile, compute GPA).

```text
┌─────────────────────────────────────────┐
│                 Student                 │
├─────────────────────────────────────────┤
│ [STATE / ATTRIBUTES]                    │
│ - name: "Aisha Muhammad"                │
│ - matric_no: "GSU/CSC/001"              │
│ - level: 300                            │
├─────────────────────────────────────────┤
│ [BEHAVIOR / METHODS]                    │
│ + display_profile()                     │
│ + promote()                             │
│ + update_email()                        │
└─────────────────────────────────────────┘
```

---

## 2. Understanding `self`: The Current Instance

In Python, every instance method must take `self` as its first parameter. 

### What is `self`?
`self` is a reference to the **specific instance** that is calling the method.

When you write:
```python
student1.display_profile()
```

Python internally transforms and executes:
```python
Student.display_profile(student1)
```

`self` is how a method knows **which** object's data to read or modify when there are 10,000 student objects in memory.

---

## 3. Creating Attributes and Methods

Let's build a basic `Student` class with attributes and behavior:

```python
class Student:
    """Represents a student with profile and level tracking."""

    def initialize(self, name: str, matric_no: str, level: int):
        """Set initial instance attributes."""
        self.name = name
        self.matric_no = matric_no
        self.level = level

    def display_profile(self):
        """Display student demographic details."""
        print(f"--- Student Profile ---")
        print(f"Name:       {self.name}")
        print(f"Matric No:  {self.matric_no}")
        print(f"Level:      {self.level}")

    def promote(self):
        """Promote student to the next academic level."""
        self.level += 100
        print(f"{self.name} has been promoted to level {self.level}!")
```

### Using the Class:
```python
s1 = Student()
s1.initialize("Aisha Muhammad", "GSU/CSC/001", 100)

s2 = Student()
s2.initialize("Musa Bello", "GSU/CSC/002", 200)

# Aisha's profile
s1.display_profile()

# Promote Aisha
s1.promote()

# Verify Musa was unaffected
print(f"Musa's level is still: {s2.level}")
```

Notice that `s1.promote()` modified `s1.level` from 100 to 200, while `s2.level` remained 200. Each instance maintains its own isolated state!

---

## 4. Under the Hood: How Method Calls Work

Why do we define `def display_profile(self):` with 1 parameter, but call `s1.display_profile()` with 0 arguments?

```python
# Syntax 1 (Normal Object-Oriented style):
s1.display_profile()

# Syntax 2 (Behind-the-scenes Procedural style):
Student.display_profile(s1)
```

Both lines do the exact same thing! In Syntax 1, Python automatically passes the object before the dot (`s1`) as the first argument (`self`) to the class function.

---

## 5. Practical Student Management Example: Dynamic Behaviors

Let's model a more realistic student with course tracking:

```python
class Student:
    def setup(self, name: str, matric_no: str):
        self.name = name
        self.matric_no = matric_no
        self.registered_courses = []

    def enroll(self, course_code: str):
        if course_code in self.registered_courses:
            print(f"Warning: {self.name} is already registered for {course_code}.")
            return
        self.registered_courses.append(course_code)
        print(f"{self.name} successfully registered for {course_code}.")

    def drop(self, course_code: str):
        if course_code not in self.registered_courses:
            print(f"Error: {self.name} is not registered for {course_code}.")
            return
        self.registered_courses.remove(course_code)
        print(f"{self.name} dropped {course_code}.")

    def get_summary(self) -> str:
        courses_str = ", ".join(self.registered_courses) if self.registered_courses else "No courses registered"
        return f"Student: {self.name} ({self.matric_no}) | Courses ({len(self.registered_courses)}): [{courses_str}]"
```

```python
# Demo
student = Student()
student.setup("Fatima Usman", "GSU/CSC/003")
student.enroll("CSC201")
student.enroll("CSC203")
student.enroll("CSC201") # Duplicate test
print(student.get_summary())

student.drop("CSC201")
print(student.get_summary())
```

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> Is `self` a Python keyword like `def` or `class`?
> *No! `self` is a standard naming convention. You could technically name it `this` or `me`, but doing so violates PEP 8 and will confuse any Python developer reading your code.*

### 💬 Discuss
> What would happen if two students registered for courses using a shared global list instead of `self.registered_courses`?

### 💻 Code Along: Proving `self` is the caller
Run this script:
```python
class IdentityDemo:
    def identify(self):
        print(f"Inside identify(), id(self) is: {hex(id(self))}")

obj = IdentityDemo()
print(f"Outside, id(obj) is:            {hex(id(obj))}")
obj.identify()
```
Notice both hexadecimal memory addresses match exactly!

### 🔍 Debug This
Find the 2 errors in this snippet:

```python
class Student:
    # Error 1: Missing self in method definition
    def set_name(name):
        # Error 2: Missing self. when setting attribute
        name = name

s = Student()
s.set_name("Zainab")
```

**Fix:**
```python
class Student:
    def set_name(self, name):
        self.name = name
```

---

## 7. Knowledge Check & Quiz

1. **What is the purpose of the `self` parameter in a method definition?**
   - A) To refer to the Python interpreter
   - B) To reference the specific instance calling the method
   - C) To make the method private
   - D) To inherit from a parent class
   *(Answer: B)*

2. **When calling `student.display_profile()`, what does Python automatically supply as the first argument?**
   - A) `Student`
   - B) `None`
   - C) `student`
   - D) `self`
   *(Answer: C)*

3. **What is the difference between an attribute and a method?**
   - A) Attributes are functions; methods are variables
   - B) Attributes represent state; methods represent behavior
   - C) Attributes require `self`; methods do not
   - D) There is no difference
   *(Answer: B)*

---

## 8. Common Mistakes
- **Forgetting `self` as the first method parameter**: Leads to `TypeError: method() takes 0 positional arguments but 1 was given`.
- **Forgetting `self.` when accessing attributes**: Writing `print(name)` inside a method searches for a local/global variable `name` instead of `self.name`.
- **Calling a method without parentheses**: Writing `student.display_profile` prints the method object reference instead of executing the method.

---

## 9. Key Takeaways
- **Attributes** store the data / state of an instance.
- **Methods** define functions that operate on that instance's data.
- **`self`** is the explicit reference to the current instance passed automatically by Python.
- Every instance created has its own isolated attribute storage in memory.

---

## 10. Homework & Exercises
- Complete [Exercise 02 — Attributes and Methods](../exercises/02-attributes-and-methods/README.md).
- Read [Lecture 04 — Constructors and Properties](04-constructors-and-properties.md).
