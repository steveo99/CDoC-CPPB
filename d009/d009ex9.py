"""
100 Days of Code, Day 9, Excercise 9
Grading Program
"""


def main():
    """
    Code for Day 9 Excercise 9
    Grading Program
    """

    student_scores = {
        "Harry": 88,
        "Ron": 78,
        "Hermione": 95,
        "Draco": 75,
        "Neville": 60,
    }

    student_grades = {}
    for key, value in student_scores.items():
        if value >= 91:
            grade = "Outstanding"
        elif value >= 81:
            grade = "Exceeds Expectations"
        elif value >= 71:
            grade = "Acceptable"
        else:
            grade = "Fail"
        student_grades[key] = grade

    print(student_grades)


if __name__ == "__main__":
    main()
