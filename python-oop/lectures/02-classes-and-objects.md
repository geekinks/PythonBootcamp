# Lecture 02 — Classes and Objects

> **Blueprints and Instances: Creating the Building Blocks of Software**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Define what a **Class** and an **Object** (Instance) are.
2. Use the blueprint analogy to reason about classes vs objects.
3. Define classes using the `class` keyword and instantiate objects.
4. Inspect objects using `type()`, `id()`, and `isinstance()`.
5. Instantiate multiple independent objects from the same class.
6. Understand memory allocation and object identity in Python.

---

## Prerequisites
- Completed [Lecture 01 — Python & OOP Introduction](01-python-oop-introduction.md).

---

## 1. Introduction: The Blueprint Analogy

Think of an architectural blueprint for a house:
- The **blueprint** is not a physical house; you cannot live inside it. It is a set of specifications, plans, and dimensions.
- The **actual house** built from that blueprint is a concrete entity made of brick and mortar.
- From a **single blueprint**, an engineer can construct **hundreds of distinct houses**. Each house has its own address, its own occupants, and its own paint color.

```text
       ┌──────────────────────────────┐
       │       Class Blueprint        │
       │       (class Student)        │
       └──────────────┬───────────────┘
                      │
       Instantiate    │   Instantiate
       ┌──────────────┴──────────────┐
       ↓                             ↓
┌──────────────┐              ┌──────────────┐
│   student1   │              │   student2   │
│ name: Aisha  │              │ name: Musa   │
│ id: 0x7f8a10 │              │ id: 0x7f8a90 │
└──────────────┘              └──────────────┘
```

In Python:
- **Class**: The user-defined blueprint / type.
- **Object / Instance**: The concrete item created in computer memory according to that blueprint.

---

## 2. Syntax: Defining a Class and Instantiating Objects

In Python, we use the `class` keyword. By convention, class names use **PascalCase** (e.g., `Student`, `CourseRegistration`, `LecturerProfile`).

```python
# The simplest possible class in Python
class Student:
    """Blueprint for a university student."""
    pass
```

### Instantiating (Creating) Objects
To create an instance of a class, call the class name followed by parentheses `()`:

```python
# Creating two distinct student objects
student1 = Student()
student2 = Student()

print(student1)
print(student2)
```

**Output example:**
```text
<__main__.Student object at 0x7f8b2c124a90>
<__main__.Student object at 0x7f8b2c124b50>
```

Notice the memory addresses (`0x7f8b...`). They are different! `student1` and `student2` are two distinct objects residing in different memory locations.

---

## 3. Object Inspection: `type()`, `id()`, and `isinstance()`

Python provides built-in tools to inspect objects at runtime:

```python
student = Student()

# 1. type() reveals what class an object was instantiated from
print(type(student))  # <class '__main__.Student'>

# 2. id() returns the unique memory identifier of the object
print(hex(id(student)))

# 3. isinstance() checks if an object is an instance of a specific class or tuple of classes
print(isinstance(student, Student))  # True
print(isinstance(student, str))      # False
print(isinstance(student, object))   # True (Everything in Python inherits from object!)
```

---

## 4. Everything in Python is an Object

In Python, functions, integers, strings, lists, and even classes themselves are first-class objects:

```python
x = 42
text = "Geekink"

print(type(x))     # <class 'int'> -> instance of class int
print(type(text))  # <class 'str'> -> instance of class str
```

When you define `class Student:`, you are creating a new custom data type in Python!

---

## 5. Practical Student Management Example

Let's model the core entities in our Student Management System blueprint:

```python
class Student:
    """Represents a student enrolled in the institution."""
    pass

class Lecturer:
    """Represents an academic staff member."""
    pass

class Course:
    """Represents a course offered in a department."""
    pass

# Creating our initial system objects
aisha = Student()
ibrahim = Student()
dr_kabir = Lecturer()
python_course = Course()

print(f"Is Aisha a Student? {isinstance(aisha, Student)}")
print(f"Is Dr. Kabir a Student? {isinstance(dr_kabir, Student)}")
print(f"Is Dr. Kabir a Lecturer? {isinstance(dr_kabir, Lecturer)}")
```

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> If `student1 = Student()` and `student2 = Student()`, what will `student1 == student2` evaluate to by default? Why?
> *Hint: By default, Python compares identity (`id(student1) == id(student2)`).*

### 💬 Discuss
> Why is it a bad idea to name a class `student_management_system` instead of `StudentManagementSystem`? What PEP 8 conventions apply?

### 💻 Code Along
Open Python and try this experiment:

```python
class Student:
    pass

s1 = Student()
s2 = s1  # Assigning reference, NOT creating a new object!
s3 = Student() # Creating a new object!

print("s1 is s2:", s1 is s2)  # True (Both point to same memory address)
print("s1 is s3:", s1 is s3)  # False (Different objects in memory)
```

### 🔍 Debug This
Look at the following snippet. Why does line 5 throw a `TypeError`?

```python
class Student:
    pass

# BUG: Forgetting the parentheses when instantiating!
s = Student  # Did not call the constructor!
print(type(s)) # <class 'type'>, s is the CLASS itself, not an instance!
```

---

## 7. Knowledge Check & Quiz

1. **What keyword is used to define a new blueprint in Python?**
   - A) `def`
   - B) `struct`
   - C) `class`
   - D) `object`
   *(Answer: C)*

2. **Given `s1 = Student()` and `s2 = Student()`, which statement is TRUE?**
   - A) `id(s1) == id(s2)`
   - B) `s1 is s2`
   - C) `isinstance(s1, Student)` is `True`
   - D) `type(s1) != type(s2)`
   *(Answer: C)*

3. **What is the PEP 8 recommended naming convention for class names?**
   - A) snake_case
   - B) camelCase
   - C) PascalCase (CapWords)
   - D) UPPER_CASE
   *(Answer: C)*

---

## 8. Common Mistakes
- **Forgetting `()` during instantiation**: Writing `s = Student` stores a reference to the class object itself, not a new instance.
- **Using snake_case for class names**: Writing `class student_record:` violates Python standard conventions.
- **Thinking assignment copies an object**: `s2 = s1` creates an alias pointing to the exact same object in memory, not a clone.

---

## 9. Key Takeaways
- A **Class** is the blueprint/type; an **Object** is the concrete instance living in memory.
- Multiple independent objects can be spawned from a single class blueprint.
- Every instance has a unique identity (`id()`) unless explicitly aliased.
- Use `isinstance()` to verify whether an object conforms to an expected type.

---

## 10. Homework & Exercises
- Complete [Exercise 01 — Classes and Objects](../exercises/01-classes-and-objects/README.md).
- Read [Lecture 03 — Attributes, Methods, and `self`](03-attributes-methods-and-self.md).
