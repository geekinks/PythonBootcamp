"""
Exercise 01: Classes and Objects (Starter)
Complete the TODO items below and run this file to test your solution.
"""

# TODO 1: Define an empty class named Student
# class Student:
#     pass
class student:
    def _init_(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department

# TODO 2: Define an empty class named Lecturer
class lecturer:
    def _init_(self,"name","department","gender"):
        self.name=name
        self.department=department
        self.gender=self.gender

# TODO 3: Define an empty class named Course

class course:
    def _init_(self,"name","code",):
        self.name=name
        self.code=code

# TODO 4: Instantiate two Student objects into variables `student1` and `student2`
student1 = None

# TODO 5: Instantiate one Lecturer object into `lecturer1`
lecturer1 = None

# TODO 6: Instantiate one Course object into `course1`
course1 = None


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    assert student1 is not None, "student1 must not be None"
    assert student2 is not None, "student2 must not be None"
    assert lecturer1 is not None, "lecturer1 must not be None"
    assert course1 is not None, "course1 must not be None"

    assert isinstance(student1, Student), "student1 must be an instance of Student"
    assert isinstance(student2, Student), "student2 must be an instance of Student"
    assert isinstance(lecturer1, Lecturer), "lecturer1 must be an instance of Lecturer"
    assert isinstance(course1, Course), "course1 must be an instance of Course"

    assert student1 is not student2, "student1 and student2 must be distinct objects in memory"

    print("All tests passed successfully! Classes and objects created correctly.")
