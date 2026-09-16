"""
Exercise 01: Classes and Objects (Solution)
Reference solution showing class definitions, instantiation, and identity checks.
"""

class Student:
    """Represents a student enrolled in the institution."""
    pass


class Lecturer:
    """Represents an academic faculty member."""
    pass


class Course:
    """Represents an academic course."""
    pass


# Instantiating objects
student1 = Student()
student2 = Student()
lecturer1 = Lecturer()
course1 = Course()


if __name__ == "__main__":
    assert isinstance(student1, Student)
    assert isinstance(student2, Student)
    assert isinstance(lecturer1, Lecturer)
    assert isinstance(course1, Course)
    assert student1 is not student2

    print("All tests passed successfully! Classes and objects created correctly.")

    # Extension demonstration
    registry = [student1, student2, lecturer1, course1]
    print("\n--- System Registry ---")
    for idx, item in enumerate(registry, 1):
        print(f"{idx}. Object: {item} | Type: {type(item).__name__} | Memory ID: {hex(id(item))}")
