# Lecture 08 — Abstraction

> **Enforcing Contracts with Abstract Base Classes (ABCs)**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Define **Abstraction** and explain how it separates *what* a component does from *how* it does it.
2. Use Python's built-in `abc` module (`ABC`, `@abstractmethod`).
3. Understand why abstract classes cannot be instantiated directly.
4. Implement concrete subclasses that satisfy abstract contracts.
5. Apply abstraction to grading engines, payment gateways, and data exporters in the Student Management System.

---

## Prerequisites
- Completed [Lecture 07 — Polymorphism](07-polymorphism.md).

---

## 1. Introduction: What is Abstraction?

In real life, when you press the accelerator pedal in a car:
- You know *what* it does: speeds up the vehicle.
- You do not need to know *how* fuel injection, electronic throttling, and cylinder firing happen under the hood.

In software engineering:
- **Abstraction** is the process of hiding implementation details and showing only the essential feature interface to the outside world.
- An **Interface / Contract** defines what methods a class MUST provide, without dictating how they must be written.

```text
               ┌───────────────────────────────┐
               │    «abstract» ResultProcessor │
               ├───────────────────────────────┤
               │ + calculate_gpa(scores) *     │
               │ + determine_standing(gpa) *   │
               └───────────────┬───────────────┘
                               │
               ┌───────────────┴───────────────┐
               ↓                               ↓
┌─────────────────────────────┐ ┌─────────────────────────────┐
│    Standard5PointGPA        │ │     PercentageProcessor     │
├─────────────────────────────┤ ├─────────────────────────────┤
│ (Implements 5.0 Nigerian /  │ │ (Implements 100% Percentage │
│  US Scale Calculations)     │ │  Grading Standard)          │
└─────────────────────────────┘ └─────────────────────────────┘
```

---

## 2. The `abc` Module in Python

Python provides the `abc` (Abstract Base Classes) module:
1. `ABC`: A helper class that marks a class as abstract.
2. `@abstractmethod`: A decorator indicating that a method **must** be overridden by concrete subclasses.

```python
from abc import ABC, abstractmethod

class ResultProcessor(ABC):
    """Abstract contract for calculating academic performance."""

    @abstractmethod
    def calculate_gpa(self, scores: dict[str, float], credits_map: dict[str, int]) -> float:
        """Calculate and return the Grade Point Average."""
        pass

    @abstractmethod
    def determine_standing(self, gpa: float) -> str:
        """Determine academic standing (e.g. First Class, In Good Standing)."""
        pass
```

---

## 3. Instantiation Rules for Abstract Classes

If a class inherits from `ABC` and contains at least one `@abstractmethod`:

### 1. You CANNOT instantiate it directly:
```python
# CRASHES!
processor = ResultProcessor()
# TypeError: Can't instantiate abstract class ResultProcessor with abstract methods calculate_gpa, determine_standing
```

### 2. Concrete subclasses MUST implement ALL abstract methods:
```python
class IncompleteProcessor(ResultProcessor):
    def calculate_gpa(self, scores, credits_map):
        return 4.0
    # Forgot to implement determine_standing!

# CRASHES!
p = IncompleteProcessor()
# TypeError: Can't instantiate abstract class IncompleteProcessor with abstract method determine_standing
```

This guarantees **contract enforcement at object creation time** rather than failing randomly at runtime!

---

## 4. Implementing Concrete Processors

Let's implement a standard 5.0 scale Nigerian university grading system:

```python
class Standard5PointGPAProcessor(ResultProcessor):
    """Concrete implementation for standard 5.0 GPA scale."""

    @staticmethod
    def score_to_grade_point(score: float) -> int:
        if score >= 70:
            return 5 # A
        elif score >= 60:
            return 4 # B
        elif score >= 50:
            return 3 # C
        elif score >= 45:
            return 2 # D
        elif score >= 40:
            return 1 # E
        return 0     # F

    def calculate_gpa(self, scores: dict[str, float], credits_map: dict[str, int]) -> float:
        if not scores:
            return 0.0

        total_quality_points = 0
        total_units = 0

        for course_code, score in scores.items():
            credit = credits_map.get(course_code, 3) # default 3 credits
            gp = self.score_to_grade_point(score)
            total_quality_points += (gp * credit)
            total_units += credit

        return round(total_quality_points / total_units, 2) if total_units > 0 else 0.0

    def determine_standing(self, gpa: float) -> str:
        if gpa >= 4.50:
            return "First Class Honours"
        elif gpa >= 3.50:
            return "Second Class Upper (2:1)"
        elif gpa >= 2.40:
            return "Second Class Lower (2:2)"
        elif gpa >= 1.50:
            return "Third Class"
        elif gpa >= 1.00:
            return "Pass"
        return "Probation / Fail"
```

### Demonstration:
```python
processor = Standard5PointGPAProcessor()

aisha_scores = {
    "CSC301": 82.0, # 5 GP * 3 = 15
    "CSC305": 65.0, # 4 GP * 3 = 12
    "MTH301": 55.0  # 3 GP * 3 = 9
}
course_credits = {"CSC301": 3, "CSC305": 3, "MTH301": 3}

gpa = processor.calculate_gpa(aisha_scores, course_credits)
standing = processor.determine_standing(gpa)

print(f"Calculated GPA: {gpa} / 5.00")
print(f"Academic Standing: {standing}")
```

---

## 5. Concrete Methods in Abstract Classes

An abstract base class can provide common helper methods alongside abstract methods:

```python
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float, reference: str) -> bool:
        pass

    # Common concrete helper method inherited by all gateways:
    def format_receipt(self, amount: float, reference: str, status: bool) -> str:
        return f"=== RECEIPT [{reference}] ===\nAmount: ₦{amount:,.2f}\nStatus: {'SUCCESS' if status else 'FAILED'}"
```

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> What is the difference between a normal base class and an Abstract Base Class (ABC)?
> *A normal base class can be instantiated directly and does not force subclasses to implement specific methods. An ABC acts as an enforceable architectural blueprint.*

### 💬 Discuss
> Why is abstraction critical when building software in large teams where 5 different engineers write different plugins or integrations?

### 💻 Code Along: Abstract Storage Contract
```python
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def save(self, entity_id: str, data: dict):
        pass

    @abstractmethod
    def get(self, entity_id: str) -> dict | None:
        pass

class InMemoryStudentRepository(BaseRepository):
    def __init__(self):
        self._db = {}

    def save(self, entity_id: str, data: dict):
        self._db[entity_id] = data
        print(f"Stored {entity_id} in memory.")

    def get(self, entity_id: str):
        return self._db.get(entity_id)

repo = InMemoryStudentRepository()
repo.save("GSU/001", {"name": "Aisha"})
print("Retrieved:", repo.get("GSU/001"))
```

### 🔍 Debug This
Why does Python fail when running this code?

```python
from abc import ABC, abstractmethod

class AuthProvider(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

class GoogleAuth(AuthProvider):
    # BUG: Forgot to implement login!
    def verify_token(self, token):
        return True

client = GoogleAuth() # TypeError!
```

---

## 7. Knowledge Check & Quiz

1. **Which Python module contains the tools for defining abstract classes?**
   - A) `abstract`
   - B) `abc`
   - C) `typing`
   - D) `sys`
   *(Answer: B)*

2. **Can you create an instance of a class that inherits from `ABC` and contains unimplemented `@abstractmethod` functions?**
   - A) Yes, always
   - B) No, Python will raise a `TypeError` at instantiation time
   - C) Yes, but calling the method returns `None`
   - D) Only inside unit tests
   *(Answer: B)*

3. **What is the primary benefit of Abstraction?**
   - A) It speeds up Python execution by 50%
   - B) It enforces a consistent interface and separates specification from implementation details
   - C) It eliminates the need for unit testing
   - D) It automatically converts Python code to C
   *(Answer: B)*

---

## 8. Common Mistakes
- **Applying `@abstractmethod` without inheriting from `ABC`**: Does NOT enforce abstraction checks at instantiation.
- **Calling `super()` without implementing the method in concrete classes**.
- **Creating ABCs for tiny 1-off scripts**: Abstraction is an architectural tool for domain boundaries, plugin systems, and team contracts.

---

## 9. Key Takeaways
- Abstraction focuses on **what** an object does rather than **how** it does it.
- Use `ABC` and `@abstractmethod` from the `abc` module to define explicit, enforceable contracts.
- An abstract class cannot be instantiated if it has unimplemented abstract methods.
- Concrete classes must satisfy all abstract methods to become instantiable.

---

## 10. Homework & Exercises
- Complete [Exercise 08 — Abstraction](../exercises/08-abstraction/README.md).
- Read [Lecture 09 — Composition, Association, and Aggregation](09-composition-association-aggregation.md).
