# Lecture 07 — Polymorphism

> **Many Forms, One Interface: The Power of Duck Typing**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Define **Polymorphism** ("many forms") and why it enables flexible, loosely coupled systems.
2. Implement polymorphism via **Method Overriding** across class hierarchies.
3. Understand Python's philosophy of **Duck Typing** ("If it walks like a duck and quacks like a duck, it's a duck").
4. Process polymorphic collections with a unified interface without checking `isinstance()` everywhere.
5. Apply polymorphism to reporting, notifications, and grading workflows.

---

## Prerequisites
- Completed [Lecture 06 — Inheritance](06-inheritance.md).

---

## 1. Introduction: What is Polymorphism?

The word *Polymorphism* comes from Greek:
- *Poly* = Many
- *Morph* = Form

In software engineering, **Polymorphism means treating different types of objects through the same uniform interface, with each object providing its own specialized behavior.**

```text
               ┌────────────────────────┐
               │    Unified Command     │
               │  user.display_profile()│
               └───────────┬────────────┘
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
   ┌───────────────────┐       ┌───────────────────┐
   │  Student Object   │       │  Lecturer Object  │
   ├───────────────────┤       ├───────────────────┤
   │ Prints matric no, │       │ Prints staff ID,  │
   │ courses, and GPA  │       │ department, rank  │
   └───────────────────┘       └───────────────────┘
```

---

## 2. Polymorphism via Inheritance and Overriding

Let's look at how polymorphic dispatch works using an inheritance hierarchy:

```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_role_description(self) -> str:
        return f"Standard user: {self.name}"

class Student(User):
    def __init__(self, name: str, email: str, matric_no: str):
        super().__init__(name, email)
        self.matric_no = matric_no

    def get_role_description(self) -> str:
        return f"Student: {self.name} (Matric: {self.matric_no})"

class Lecturer(User):
    def __init__(self, name: str, email: str, staff_id: str):
        super().__init__(name, email)
        self.staff_id = staff_id

    def get_role_description(self) -> str:
        return f"Lecturer: {self.name} (Staff ID: {self.staff_id})"

class Admin(User):
    def get_role_description(self) -> str:
        return f"System Administrator: {self.name} [ROOT ACCESS]"
```

### The Polymorphic Collection:
Notice how the calling code does **not** care whether an element is a `Student`, `Lecturer`, or `Admin`. It simply invokes `get_role_description()`:

```python
community_members = [
    Student("Aisha", "aisha@uni.edu", "GSU/CSC/001"),
    Lecturer("Dr. Kabir", "kabir@uni.edu", "STF-402"),
    Admin("System Manager", "admin@uni.edu"),
    Student("Musa", "musa@uni.edu", "GSU/CSC/002"),
]

print("--- University Directory ---")
for member in community_members:
    # Polymorphic call: Same interface, different behavior!
    print(member.get_role_description())
```

---

## 3. Python's Duck Typing Philosophy

In statically typed languages (like Java, C++, or C#), polymorphism requires an explicit parent class or interface.

Python uses **Duck Typing**:
> *"If it walks like a duck and quacks like a duck, it's a duck."*

In Python, as long as an object provides the expected method or attribute, Python will execute it — **the classes don't even need to share a common parent class!**

### Example: Polymorphic Notification Senders
```python
class EmailNotifier:
    def send(self, recipient: str, message: str):
        print(f"📧 Sending Email to {recipient}: {message}")

class SMSNotifier:
    def send(self, recipient: str, message: str):
        print(f"📱 Sending SMS to {recipient}: {message}")

class PushNotifier:
    def send(self, recipient: str, message: str):
        print(f"🔔 Sending Push Notification to {recipient}: {message}")

# Function that accepts ANY object with a send(recipient, message) method:
def broadcast_alert(notifiers: list, recipient: str, alert_message: str):
    for notifier in notifiers:
        notifier.send(recipient, alert_message)

# Usage:
channels = [EmailNotifier(), SMSNotifier(), PushNotifier()]
broadcast_alert(channels, "Aisha", "Your exam timetable has been published.")
```

None of the three classes inherit from a common `Notifier` parent, yet Python executes them seamlessly because all three implement `.send(...)`.

---

## 4. The Anti-Pattern: Explicit Type Checking

Beginners often write code with chains of `if isinstance(...)`:

### ❌ Bad (Rigid & Fragile):
```python
def print_badge(person):
    if isinstance(person, Student):
        print(f"STUDENT BADGE: {person.name} ({person.matric_no})")
    elif isinstance(person, Lecturer):
        print(f"STAFF BADGE: {person.name} ({person.staff_id})")
    elif isinstance(person, Admin):
        print(f"ADMIN BADGE: {person.name}")
    # Adding a new role requires editing this function every time!
```

### ✅ Good (Polymorphic & Open for Extension):
```python
def print_badge(person):
    # Delegate rendering to the object itself!
    print(person.get_badge_text())
```

---

## 5. Interactive Learning & Activities

### 🤔 Think About It
> What happens if you pass an object that does NOT have the expected method to a duck-typed function?
> *Python raises `AttributeError: 'X' object has no attribute 'method_name'`. In Lecture 08, we will learn how **Abstraction (ABCs)** guarantees that methods are implemented at startup!*

### 💬 Discuss
> Why does eliminating `if isinstance(...)` chains make systems much easier to maintain and extend?

### 💻 Code Along: Polymorphic Course Fee Calculator
```python
class UndergraduateCourse:
    def __init__(self, code: str, credits: int):
        self.code = code
        self.credits = credits

    def calculate_tuition(self) -> float:
        return self.credits * 1500.0

class PostgraduateCourse:
    def __init__(self, code: str, credits: int):
        self.code = code
        self.credits = credits

    def calculate_tuition(self) -> float:
        return (self.credits * 3000.0) + 10000.0 # higher rate + lab fee

courses = [
    UndergraduateCourse("CSC301", 3),
    PostgraduateCourse("CSC801", 4),
    UndergraduateCourse("CSC305", 2)
]

total_fees = sum(c.calculate_tuition() for c in courses)
print(f"Total Tuition Due: ₦{total_fees:,.2f}")
```

### 🔍 Debug This
Why does this polymorphic loop fail?

```python
class PDFExporter:
    def export(self, data):
        return f"Exporting {data} to PDF"

class CSVExporter:
    # BUG: Method name mismatch! Named export_csv instead of export
    def export_csv(self, data):
        return f"Exporting {data} to CSV"

for exp in [PDFExporter(), CSVExporter()]:
    print(exp.export("Student Records"))
```

---

## 6. Knowledge Check & Quiz

1. **What is the core principle of Duck Typing in Python?**
   - A) All classes must inherit from `Duck`
   - B) Object suitability is determined by the presence of methods/attributes, not explicit inheritance
   - C) Code must be compiled ahead of time
   - D) Only strings and lists can be passed to functions
   *(Answer: B)*

2. **Why is relying on polymorphism preferred over long `if isinstance(...)` chains?**
   - A) It makes the code faster to download
   - B) It allows new classes to be added without modifying existing consumer code (Open/Closed Principle)
   - C) It eliminates the need for constructors
   - D) It prevents memory usage
   *(Answer: B)*

3. **What happens if a method is called on an object that does not define it?**
   - A) `SyntaxError`
   - B) `AttributeError`
   - C) Returns `None`
   - D) Reboots the script
   *(Answer: B)*

---

## 7. Common Mistakes
- **Writing `if isinstance(...)` chains everywhere**: Breaks extensibility.
- **Inconsistent method signatures in polymorphic classes**: Having one class accept `export(data)` and another accept `export(data, format, destination)`.
- **Assuming polymorphism requires inheritance in Python**: Duck typing allows unrelated classes with compatible signatures to act polymorphically.

---

## 8. Key Takeaways
- Polymorphism allows different classes to share a uniform interface while implementing distinct behaviors.
- In Python, polymorphism is achieved via method overriding in subclasses and **Duck Typing** across unrelated classes.
- Design code to interact with *capabilities* (interfaces) rather than *concrete types*.

---

## 9. Homework & Exercises
- Complete [Exercise 07 — Polymorphism](../exercises/07-polymorphism/README.md).
- Read [Lecture 08 — Abstraction](08-abstraction.md).
