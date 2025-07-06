students = {}

while ":" in (line := input()):

    student_info = line.split(":")

    for i in range(0, len(student_info), 3):
        student_name = student_info[i]
        student_id = student_info[i + 1]
        student_course = student_info[i + 2]

        students[student_name] = [student_id, student_course]

old_line = line.split("_")
new_line = " ".join(old_line)

for info in students.items():
    name = info[0]
    student_id = info[1][0]
    course = info[1][1]
    if new_line == course:
        print(f"{name} - {student_id}")