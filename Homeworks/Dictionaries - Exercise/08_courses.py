register = {}

while "end" not in (line := input().split(" : ")):
    course_name = line[0]
    student_name = line[1]

    if course_name not in register:
        register[course_name] = {}

    register[course_name][student_name] = None

for course, students in register.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")