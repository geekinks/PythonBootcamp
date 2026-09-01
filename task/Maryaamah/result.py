
def calculate_result(scores):

    total = sum(scores)

    average = total / len(scores)

    grade = calculate_grade(average)

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, average, grade, result
