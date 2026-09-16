# Lecture 05 — Encapsulation

> **Information Hiding and Protecting Object Invariants**

## Learning Objectives
By the end of this lecture, you will be able to:
1. Define **Encapsulation** and explain why it is the cornerstone of robust object-oriented systems.
2. Explain Python's visibility conventions: Public (`name`), Protected (`_name`), and Private (`__name`).
3. Understand **name mangling** and how Python implements privacy.
4. Distinguish between hard privacy (as in C++/Java) and Python's "we are all consenting adults here" philosophy.
5. Protect object invariants and validate internal state mutations.

---

## Prerequisites
- Completed [Lecture 04 — Constructors and Properties](04-constructors-and-properties.md).

---

## 1. Introduction: What is Encapsulation?

Encapsulation has two fundamental aspects:
1. **Bundling**: Packaging related data (attributes) and behavior (methods) together into a single unit.
2. **Access Control / Information Hiding**: Restricting direct external access to an object's internal representation to prevent unintended corruption and maintain internal invariants.

```text
┌────────────────────────────────────────────────────────┐
│                   PUBLIC INTERFACE                     │
│  - enroll_course(course)                               │
│  - record_score(course_code, score)                    │
│  - get_gpa()                                           │
├────────────────────────────────────────────────────────┤
│             PROTECTED / PRIVATE INTERNALS              │
│  - _scores: {"CSC301": 85, "CSC305": 92}               │
│  - _calculate_grade_point(score)                       │
│  - __encryption_key: 0x9AFB                            │
└────────────────────────────────────────────────────────┘
```

---

## 2. Python's Access Control Conventions

Unlike Java or C++ with rigid keywords like `private`, `protected`, and `public`, Python relies on **naming conventions**:

| Naming Format | Convention | Intended Scope | Behavior in Python |
| :--- | :--- | :--- | :--- |
| `name` | **Public** | Anywhere | Accessible by anyone, anywhere. |
| `_name` | **Protected** | Internal to class & subclasses | **Convention only**. Signals "internal detail, do not touch externally". |
| `__name` | **Private** | Strictly internal to this class | Python **mangles** the name to `_ClassName__name` to prevent accidental subclass collisions. |

---

## 3. Protecting Invariants: The Scores Example

An **invariant** is a condition that must always remain true throughout the lifetime of an object.
For example: *"A student's score in any course must always be a number between 0 and 100."*

### Unencapsulated (Dangerous):
```python
class Student:
    def __init__(self, name: str):
        self.name = name
        self.scores = {} # Public dictionary

s = Student("Aisha")
# Anyone can corrupt internal state:
s.scores["CSC301"] = -9999
s.scores["CSC305"] = "Incomplete"
```

### Encapsulated (Safe):
```python
class Student:
    """Represents a student with protected score records."""

    def __init__(self, name: str, matric_no: str):
        self.name = name
        self.matric_no = matric_no
        self._scores = {} # Protected attribute

    def add_score(self, course_code: str, score: float):
        """Add or update a score with strict boundary validation."""
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a numerical value.")
        if not (0 <= score <= 100):
            raise ValueError(f"Score {score} is invalid. Must be between 0 and 100.")
        
        self._scores[course_code] = float(score)

    def get_score(self, course_code: str) -> float | None:
        """Read-only access to a specific score."""
        return self._scores.get(course_code)

    def get_average_score(self) -> float:
        """Calculate average across all recorded courses."""
        if not self._scores:
            return 0.0
        return sum(self._scores.values()) / len(self._scores)
```

Now, the class itself guarantees that `_scores` will **never** contain negative numbers, non-numeric types, or values exceeding 100.

---

## 4. Name Mangling: Double Underscore (`__private`)

When you prefix an attribute with two leading underscores (and at most one trailing underscore), Python triggers **name mangling**:

```python
class Account:
    def __init__(self, owner: str, pin: str):
        self.owner = owner
        self.__pin = pin # Private attribute

    def verify_pin(self, attempt: str) -> bool:
        return self.__pin == attempt

acc = Account("Aisha", "1234")
print(acc.owner) # Works!

# Trying to access __pin directly:
try:
    print(acc.__pin)
except AttributeError as err:
    print(f"Direct access failed: {err}")

# How Python mangled it:
print(f"Mangled attribute name: {acc._Account__pin}") # Exists as _Account__pin
```

### Why does name mangling exist?
The main purpose of name mangling is **not security**, but rather **avoiding naming collisions in deep inheritance trees** when child classes might accidentally use the same variable name.

---

## 5. Python Philosophy: "We Are All Consenting Adults Here"

Python does not create impenetrable walls around object attributes. If a developer explicitly writes `acc._Account__pin`, Python will let them access it.

Python's philosophy is:
> *"We are all consenting adults here."*
> If an attribute starts with an underscore `_`, it is a contract warning that you are bypassing the public API and risk breaking on future internal updates.

---

## 6. Interactive Learning & Activities

### 🤔 Think About It
> Why is returning a direct reference to a mutable internal list (e.g. `return self._courses`) a potential encapsulation leak? How can you fix it?
> *Fix: Return a copy or tuple: `return list(self._courses)` or `return tuple(self._courses)` so callers cannot mutate your internal list without calling your methods!*

### 💬 Discuss
> In a banking application, should `balance` be a public attribute, a protected attribute with a getter property, or only modified via `deposit()` and `withdraw()` methods?

### 💻 Code Along: Preventing Mutable Leaks
```python
class StudentRegistry:
    def __init__(self):
        self._students = []

    def register(self, name: str):
        self._students.append(name)

    @property
    def all_students(self) -> list[str]:
        # Defensive copy prevents external callers from clearing our list!
        return self._students.copy()

reg = StudentRegistry()
reg.register("Aisha")
reg.register("Muhammad")

# External attempt to tamper:
external_list = reg.all_students
external_list.clear() # Cleared the copy!

print("Registry intact:", reg.all_students) # Still contains Aisha and Muhammad!
```

### 🔍 Debug This
What is wrong with this encapsulation attempt?

```python
class SecureWallet:
    def __init__(self, initial_amount: float):
        # BUG: Typo with trailing double underscores turns off name mangling!
        # __name__ is reserved for Python special methods/attributes!
        self.__balance__ = initial_amount

wallet = SecureWallet(500)
wallet.__balance__ = -99999 # Accidentally public!
```

---

## 7. Knowledge Check & Quiz

1. **In Python, what is the convention for indicating an attribute is for internal use only?**
   - A) Prefixing with `private `
   - B) A single leading underscore (e.g., `_score`)
   - C) Capitalizing the attribute name
   - D) Suffixing with `.internal`
   *(Answer: B)*

2. **What does Python do under the hood to an attribute named `__matric_no` in class `Student`?**
   - A) Deletes it from memory
   - B) Mangles it to `_Student__matric_no`
   - C) Locks the OS memory page
   - D) Converts it to a constant
   *(Answer: B)*

3. **What is an "invariant" in software design?**
   - A) A variable that changes on every loop iteration
   - B) A rule or condition that must always remain valid for an object
   - C) An abstract class
   - D) A decorator
   *(Answer: B)*

---

## 8. Common Mistakes
- **Naming attributes with double leading AND double trailing underscores** (e.g., `__balance__`): This naming pattern is reserved for Python built-ins (dunder methods like `__init__`) and will NOT be mangled.
- **Leaking internal mutable collections**: Returning internal lists or dicts directly, allowing external modification without validation.
- **Overusing `__private` when `_protected` is sufficient**: In Python, single underscore `_` is idiomatic and sufficient 95% of the time.

---

## 9. Key Takeaways
- Encapsulation groups data + methods and protects the internal state from illegal mutations.
- Single underscore `_var` indicates protected/internal convention.
- Double underscore `__var` invokes name mangling (`_ClassName__var`) to prevent naming collisions.
- Always validate inputs at the public boundary (`add_score`, property setters) to keep internal invariants safe.

---

## 10. Homework & Exercises
- Complete [Exercise 05 — Encapsulation](../exercises/05-encapsulation/README.md).
- Read [Lecture 06 — Inheritance](06-inheritance.md).
