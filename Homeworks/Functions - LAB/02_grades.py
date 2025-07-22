def grades(student_grade):
    if 2 <= student_grade < 3:
        return "Fail"
    elif 3 <= student_grade < 3.5:
        return "Poor"
    elif 3.5 <= student_grade < 4.5:
        return "Good"
    elif 4.5 <= student_grade < 5.5:
        return "Very Good"
    elif 5.5 <= student_grade <= 6:
        return "Excellent"

grade = float(input())
print(grades(grade))