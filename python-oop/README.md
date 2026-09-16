# 🐍 Python Object-Oriented Programming (OOP) & System Design

> **A Complete, Practical, Beginner-to-Intermediate Curriculum for Mastering OOP in Python**

Welcome to the **Python OOP Masterclass** repository — a comprehensive, hands-on curriculum built for interns, computer science students, and software engineers transitioning from basic scripting to professional system modeling.

---

## 🎯 Learning Philosophy

> **"Don't just write classes — learn to model problems."**

Most courses teach Object-Oriented Programming as dry definitions:
`Class -> Object -> Inheritance -> Polymorphism -> Done`.

This curriculum teaches you to think like a software architect:

```text
Syntax
   ↓
Code
   ↓
Objects
   ↓
Design
   ↓
Architecture
   ↓
Systems
```

When confronted with a software challenge, we train you to ask:

```text
What problem are we solving?
            ↓
What entities exist in the domain?
            ↓
What data (state) belongs to each entity?
            ↓
What behaviors (methods) should each entity perform?
            ↓
What invariants must be protected?
            ↓
How do entities relate (IS-A, HAS-A, USES-A)?
            ↓
What classes and abstractions should be designed?
            ↓
A Working, Maintainable, Tested System!
```

The **Student Management System (SMS)** serves as our primary running domain example across all lectures, exercises, and architectural milestones.

---

## 🗺️ Course Roadmap

```text
01. Python & OOP Introduction
       ↓
02. Classes & Objects (Blueprints & Identity)
       ↓
03. Attributes, Methods, and `self`
       ↓
04. Constructors (`__init__`) and Properties (`@property`, `@setter`)
       ↓
05. Encapsulation & Protecting Invariants (`_protected`, `__private`)
       ↓
06. Inheritance & `super()` (IS-A Relationships)
       ↓
07. Polymorphism & Duck Typing (Unified Interfaces)
       ↓
08. Abstraction & Abstract Base Classes (`ABC`, `@abstractmethod`)
       ↓
09. Composition, Association, and Aggregation (HAS-A vs IS-A)
       ↓
10. Class Methods (`@classmethod`) & Static Methods (`@staticmethod`)
       ↓
11. OOP Design Principles (S.O.L.I.D.)
       ↓
12. OOP Design with the Student Management System
       ↓
13. Final Capstone Project & Defense
```

---

## 📚 Curriculum & Lectures

| Lecture | Topic | Core Takeaways |
| :--- | :--- | :--- |
| [**Lecture 01**](lectures/01-python-oop-introduction.md) | Python & OOP Introduction | Multi-paradigm Python, Procedural vs OOP, State sprawl problems |
| [**Lecture 02**](lectures/02-classes-and-objects.md) | Classes and Objects | Blueprints vs Instances, `type()`, `id()`, `isinstance()`, memory identity |
| [**Lecture 03**](lectures/03-attributes-methods-and-self.md) | Attributes, Methods & `self` | Instance state, method behaviors, how Python translates `obj.method()` |
| [**Lecture 04**](lectures/04-constructors-and-properties.md) | Constructors & Properties | `__init__` constructor, default values, `@property` getters, `@setter` validation |
| [**Lecture 05**](lectures/05-encapsulation.md) | Encapsulation | Protected attributes (`_`), name mangling (`__`), protecting invariants |
| [**Lecture 06**](lectures/06-inheritance.md) | Inheritance & `super()` | Base & derived classes, `super()` delegation, method overriding |
| [**Lecture 07**](lectures/07-polymorphism.md) | Polymorphism & Duck Typing | Unified interfaces, Duck Typing, polymorphic collections |
| [**Lecture 08**](lectures/08-abstraction.md) | Abstraction & ABCs | `abc` module, `ABC`, `@abstractmethod`, contract enforcement |
| [**Lecture 09**](lectures/09-composition-association-aggregation.md) | Object Relationships | Favoring Composition over Inheritance, HAS-A vs IS-A vs USES |
| [**Lecture 10**](lectures/10-class-static-methods.md) | Class & Static Methods | `self` vs `cls`, `@classmethod` factory constructors, `@staticmethod` |
| [**Lecture 11**](lectures/11-oop-design-principles.md) | OOP Design Principles (SOLID) | Single Responsibility, Open/Closed, Liskov, Interface Segregation, DIP |
| [**Lecture 12**](lectures/12-oop-design-student-management-system.md) | End-to-End System Modeling | Domain entity extraction, UML class diagrams, architectural layers |
| [**Lecture 13**](lectures/13-final-project.md) | Final Capstone Synthesis | Evaluation rubric, architectural defense, portfolio project guidelines |

---

## 🧪 Practical Hands-On Exercises

Every major topic includes an exercise directory with a scenario `README.md`, a `starter.py` scaffold with test assertions, and a complete `solution.py`.

```text
exercises/
├── 01-classes-and-objects/              🟢 Beginner
├── 02-attributes-and-methods/           🟢 Beginner
├── 03-constructors-and-self/            🟢 Beginner
├── 04-properties/                       🟡 Intermediate
├── 05-encapsulation/                    🟡 Intermediate
├── 06-inheritance/                      🟡 Intermediate
├── 07-polymorphism/                     🟡 Intermediate
├── 08-abstraction/                      🔴 Challenge
├── 09-composition/                      🔴 Challenge
└── 10-oop-design/                       🔴 Challenge
```

👉 **Get started with [exercises/README.md](exercises/README.md)**.

---

## 🏗️ Reference Project: Student Management System (SMS)

A complete, production-grade reference implementation demonstrating the entire curriculum in action.

```text
projects/student-management-system/
├── Readme.md              # Project overview and documentation
├── requirements.md        # Formal requirements specification
├── architecture.md        # Architectural subsystems and data flow
├── design.md              # Detailed UML diagrams and design decisions
├── src/                   # Python package implementation
│   ├── user.py            # Base User abstract class
│   ├── student.py         # Student entity (inherits User, composes Result & Attendance)
│   ├── lecturer.py        # Lecturer entity (inherits User, teaches courses)
│   ├── course.py          # Course & Department catalog
│   ├── result.py          # Result manager & Strategy ResultProcessor ABC
│   ├── attendance.py      # Attendance tracker and exam qualification
│   └── main.py            # Interactive CLI application
├── tests/                 # 100% standard unit test suite
└── examples/              # Quickstart and advanced workflow scripts
```

### Running the Project:
```bash
# 1. Run the interactive demonstration
python3 -m projects.student-management-system.src.main

# 2. Run the complete automated test suite
cd projects/student-management-system
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## 📝 Capstone Assignments

Challenge yourself with four extensive real-world domain design assignments in [`projects/assignments/`](projects/assignments/README.md):

1. [**Library Management System**](projects/assignments/01-library-management-system.md) — Catalog state, member borrowing limits, availability invariants.
2. [**Food Delivery System**](projects/assignments/02-food-delivery-system.md) — Multi-entity collaboration, order state machines, driver dispatch.
3. [**E-Commerce Platform**](projects/assignments/03-ecommerce-system.md) — Cart composition, inventory protection, polymorphic payment gateways.
4. [**Learning Management System (LMS)**](projects/assignments/04-lms-design-challenge.md) — Course hierarchies, auto-graded quizzes, certificate issuance.

---

## 📂 Repository Structure

```text
python-oop/
│
├── README.md                                  # Repository overview (this file)
│
├── lectures/                                  # Complete lecture series (13 chapters)
│   ├── 01-python-oop-introduction.md
│   ├── 02-classes-and-objects.md
│   ├── 03-attributes-methods-and-self.md
│   ├── 04-constructors-and-properties.md
│   ├── 05-encapsulation.md
│   ├── 06-inheritance.md
│   ├── 07-polymorphism.md
│   ├── 08-abstraction.md
│   ├── 09-composition-association-aggregation.md
│   ├── 10-class-static-methods.md
│   ├── 11-oop-design-principles.md
│   ├── 12-oop-design-student-management-system.md
│   └── 13-final-project.md
│
├── exercises/                                 # Hands-on coding exercises
│   ├── README.md
│   ├── 01-classes-and-objects/                (README.md, starter.py, solution.py)
│   ├── 02-attributes-and-methods/             (README.md, starter.py, solution.py)
│   ├── 03-constructors-and-self/              (README.md, starter.py, solution.py)
│   ├── 04-properties/                         (README.md, starter.py, solution.py)
│   ├── 05-encapsulation/                      (README.md, starter.py, solution.py)
│   ├── 06-inheritance/                        (README.md, starter.py, solution.py)
│   ├── 07-polymorphism/                       (README.md, starter.py, solution.py)
│   ├── 08-abstraction/                        (README.md, starter.py, solution.py)
│   ├── 09-composition/                        (README.md, starter.py, solution.py)
│   └── 10-oop-design/                         (README.md, starter.py, solution.py)
│
└── projects/
    ├── assignments/                           # Major course assignments
    │   ├── README.md
    │   ├── 01-library-management-system.md
    │   ├── 02-food-delivery-system.md
    │   ├── 03-ecommerce-system.md
    │   └── 04-lms-design-challenge.md
    │
    └── student-management-system/             # Complete reference implementation
        ├── Readme.md
        ├── requirements.md
        ├── architecture.md
        ├── design.md
        ├── src/
        │   ├── __init__.py
        │   ├── user.py
        │   ├── course.py
        │   ├── student.py
        │   ├── lecturer.py
        │   ├── result.py
        │   ├── attendance.py
        │   └── main.py
        ├── tests/
        │   ├── __init__.py
        │   ├── test_student.py
        │   ├── test_lecturer.py
        │   ├── test_course.py
        │   ├── test_result.py
        │   ├── test_attendance.py
        │   └── test_polymorphism.py
        └── examples/
            ├── basic_usage.py
            └── advanced_workflow.py
```

---

## 🤝 Contribution Guidelines
Contributions are welcome! If you find a typo or want to contribute an additional exercise or real-world example:
1. Fork this repository.
2. Create your feature branch (`git checkout -b feature/new-exercise`).
3. Ensure all existing tests pass (`python3 -m unittest discover`).
4. Commit your changes following standard conventional commits.
5. Push to your branch and open a Pull Request.

---

## 📄 License
This educational repository is open-sourced under the **MIT License**. Feel free to use, modify, and distribute these materials for teaching, bootcamps, and personal learning.
