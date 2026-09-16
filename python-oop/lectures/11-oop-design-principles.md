# Lecture 11 — OOP Design Principles (SOLID)

> **Architecting Robust, Maintainable, and Evolvable Software Systems**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Explain why design principles matter as codebases grow.
2. Understand each letter of the **S.O.L.I.D.** acronym with practical Python examples:
   - **S**: Single Responsibility Principle (SRP)
   - **O**: Open/Closed Principle (OCP)
   - **L**: Liskov Substitution Principle (LSP)
   - **I**: Interface Segregation Principle (ISP)
   - **D**: Dependency Inversion Principle (DIP)
3. Identify "Code Smells" (God classes, fragile base classes, tight coupling) and refactor them.
4. Apply SOLID thinking to the Student Management System.

---

## Prerequisites
- Completed Lectures 01 through 10.

---

## 1. Why Design Principles?

Writing code that merely *works* is easy. Writing code that **can be modified 6 months later without introducing 10 new bugs** requires intentional design.

```text
BAD DESIGN                        BETTER DESIGN
┌─────────────────────────┐       ┌─────────────┐   ┌─────────────┐
│       God Class         │       │   Student   │   │ GradeReport │
│ - Stores student data   │  ──>  │ - State     │   │ - Formats   │
│ - Connects to database  │       └──────┬──────┘   └─────────────┘
│ - Formats PDF reports   │              │          ┌─────────────┐
│ - Sends SMS messages    │              └────────> │ Notification│
│ - Charges tuition fees  │                         │ - Sends     │
└─────────────────────────┘                         └─────────────┘
```

---

## 2. The SOLID Principles Explained

---

### 2.1 Single Responsibility Principle (SRP)
> *"A class should have one, and only one, reason to change."*

#### ❌ BAD DESIGN (Violating SRP):
```python
class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    # Responsibility 1: Student domain logic
    def get_details(self): return f"{self.name} <{self.email}>"

    # Responsibility 2: Database persistence
    def save_to_database(self):
        print(f"Connecting to MySQL... INSERT INTO students VALUES ('{self.name}')")

    # Responsibility 3: Formatting reports
    def generate_pdf_transcript(self):
        print(f"Rendering PDF layout for {self.name}...")

    # Responsibility 4: External communication
    def send_welcome_email(self):
        print(f"Connecting to SMTP server... sending to {self.email}")
```
*Why this is bad:* If the database schema changes, `Student` changes. If the PDF template changes, `Student` changes. If email moves to SendGrid, `Student` changes.

#### ✅ REFACTORED (Adhering to SRP):
```python
# 1. Domain Entity
class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

# 2. Persistence Service
class StudentRepository:
    def save(self, student: Student):
        print(f"Saving student {student.name} to Database.")

# 3. Presentation Service
class TranscriptReporter:
    def render_pdf(self, student: Student) -> str:
        return f"=== Official Transcript: {student.name} ==="

# 4. Notification Service
class EmailService:
    def send_welcome(self, student: Student):
        print(f"Sending welcome email to {student.email}")
```

---

### 2.2 Open/Closed Principle (OCP)
> *"Software entities should be open for extension, but closed for modification."*

You should be able to add new features or behaviors without changing existing, tested code.

#### ❌ BAD DESIGN (Violating OCP):
```python
class TuitionCalculator:
    def calculate(self, student_type: str, units: int) -> float:
        if student_type == "undergraduate":
            return units * 1000.0
        elif student_type == "postgraduate":
            return units * 2500.0
        elif student_type == "international":
            return units * 5000.0
        # Adding 'scholarship' or 'part_time' requires MODIFING this function!
```

#### ✅ REFACTORED (Adhering to OCP with Polymorphism):
```python
from abc import ABC, abstractmethod

class TuitionStrategy(ABC):
    @abstractmethod
    def calculate_tuition(self, units: int) -> float:
        pass

class UndergraduateTuition(TuitionStrategy):
    def calculate_tuition(self, units: int) -> float:
        return units * 1000.0

class InternationalTuition(TuitionStrategy):
    def calculate_tuition(self, units: int) -> float:
        return units * 5000.0

# Adding a new Scholarship rate NEVER touches existing code!
class ScholarshipTuition(TuitionStrategy):
    def calculate_tuition(self, units: int) -> float:
        return (units * 1000.0) * 0.20 # 80% discount
```

---

### 2.3 Liskov Substitution Principle (LSP)
> *"Subtypes must be substitutable for their base types without altering system correctness."*

If a function expects a `User`, it should work seamlessly with a `Student` or `Lecturer` without crashing or unexpected edge cases.

#### ❌ BAD DESIGN (Violating LSP):
```python
class User:
    def send_email(self, message: str):
        print(f"Email sent: {message}")

class GuestStudent(User):
    def send_email(self, message: str):
        # Breaks contract! Caller expects send_email to succeed.
        raise PermissionError("Guest students do not have email accounts!")
```

#### ✅ REFACTORED (Adhering to LSP):
```python
class BaseUser:
    def __init__(self, username: str):
        self.username = username

class ContactableUser(BaseUser):
    def __init__(self, username: str, email: str):
        super().__init__(username)
        self.email = email

    def send_email(self, message: str):
        print(f"Sending email to {self.email}: {message}")

class GuestUser(BaseUser):
    """Guest does not advertise email capability."""
    pass
```

---

### 2.4 Interface Segregation Principle (ISP)
> *"Clients should not be forced to depend upon interfaces they do not use."*

Prefer small, focused interfaces over large "fat" interfaces.

#### ❌ BAD DESIGN (Fat Interface):
```python
from abc import ABC, abstractmethod

class AcademicOperations(ABC):
    @abstractmethod
    def enroll_course(self): pass

    @abstractmethod
    def teach_course(self): pass

    @abstractmethod
    def grade_exam(self): pass

    @abstractmethod
    def submit_assignment(self): pass

# Student is forced to implement teach_course and grade_exam!
```

#### ✅ REFACTORED (Segregated Interfaces):
```python
class Learner(ABC):
    @abstractmethod
    def enroll_course(self, course): pass

    @abstractmethod
    def submit_assignment(self, assignment): pass

class Instructor(ABC):
    @abstractmethod
    def teach_course(self, course): pass

    @abstractmethod
    def grade_exam(self, submission): pass
```

---

### 2.5 Dependency Inversion Principle (DIP)
> *"High-level modules should not depend on low-level modules. Both should depend on abstractions."*

#### ❌ BAD DESIGN (Tight Coupling):
```python
class MySQLDatabase:
    def save_data(self, data): print("Writing to MySQL...")

class RegistrationService:
    def __init__(self):
        # Directly hardcodes MySQL low-level dependency!
        self.db = MySQLDatabase()

    def register(self, student_data):
        self.db.save_data(student_data)
```

#### ✅ REFACTORED (Adhering to DIP with Dependency Injection):
```python
class DatabaseInterface(ABC):
    @abstractmethod
    def save_data(self, data): pass

class MySQLDatabase(DatabaseInterface):
    def save_data(self, data): print("Writing to MySQL...")

class MongoDatabase(DatabaseInterface):
    def save_data(self, data): print("Writing to MongoDB...")

class RegistrationService:
    # High-level module depends on the abstraction (interface), injected via constructor!
    def __init__(self, database: DatabaseInterface):
        self.db = database

    def register(self, student_data):
        self.db.save_data(student_data)

# Flexible at runtime:
service1 = RegistrationService(MySQLDatabase())
service2 = RegistrationService(MongoDatabase())
```

---

## 3. Interactive Learning & Activities

### 🤔 Think About It
> When should you refactor to SOLID? Should you design a 10-class SOLID hierarchy for a simple 30-line script?
> *Design principles should be applied proportionally to complexity. Don't over-engineer simple scripts; apply SOLID as systems grow and requirements evolve.*

### 💬 Discuss
> How does Dependency Inversion (DIP) make automated Unit Testing 10x easier?
> *(Hint: Injecting Mock/Fake repositories instead of connecting to real databases).*

---

## 4. Knowledge Check & Quiz

1. **What does the Single Responsibility Principle (SRP) state?**
   - A) Every file must contain only one function
   - B) A class should have one, and only one, reason to change
   - C) Inheritance must never be used
   - D) All attributes must be private
   *(Answer: B)*

2. **Which principle states that subclasses should be substitutable for their parent classes without breaking functionality?**
   - A) SRP
   - B) OCP
   - C) LSP (Liskov Substitution Principle)
   - D) DIP
   *(Answer: C)*

3. **In Dependency Inversion (DIP), what should high-level classes depend on?**
   - A) Concrete low-level classes
   - B) Global variables
   - C) Abstractions / Interfaces
   - D) Third-party C extensions
   *(Answer: C)*

---

## 5. Key Takeaways
- **S**: Single Responsibility (Do one job well).
- **O**: Open/Closed (Extend behavior without modifying existing code).
- **L**: Liskov Substitution (Subclasses must honor parent contracts).
- **I**: Interface Segregation (Small, focused interfaces over fat ones).
- **D**: Dependency Inversion (Depend on abstractions, inject dependencies).

---

## 6. Homework
- Read [Lecture 12 — OOP Design with Student Management System](12-oop-design-student-management-system.md).
- Read [Lecture 13 — Final Capstone Project](13-final-project.md).
