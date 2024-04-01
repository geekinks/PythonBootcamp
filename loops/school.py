student_names = []
student_grades = []


def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)

def cal_average_grade():
    return sum(student_grades) / len(student_grades)

def display_students():
    print("Student names and grades:")
    for name, grade in zip(student_names, student_grades):
        print(f"\t{name} : {grade}")

    

if __name__ == "__main__":
    pass 

    