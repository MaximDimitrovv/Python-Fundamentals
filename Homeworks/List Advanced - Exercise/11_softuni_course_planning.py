def add_lesson(schedule, lesson):
    if lesson not in schedule:
        schedule.append(lesson)

def insert_lesson(schedule, lesson, index):
    if lesson not in schedule:
        schedule.insert(index, lesson)

def remove_lesson(schedule, lesson):
    if lesson in schedule:
        schedule.remove(lesson)
    exercise = f"{lesson}-Exercise"
    if exercise in schedule:
        schedule.remove(exercise)

def swap_lessons(schedule, lesson1, lesson2):
    if lesson1 in schedule and lesson2 in schedule:
        idx1, idx2 = schedule.index(lesson1), schedule.index(lesson2)
        schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]

        exercise1 = f"{lesson1}-Exercise"
        exercise2 = f"{lesson2}-Exercise"

        if exercise1 in schedule:
            schedule.remove(exercise1)
            schedule.insert(schedule.index(lesson1) + 1, exercise1)

        if exercise2 in schedule:
            schedule.remove(exercise2)
            schedule.insert(schedule.index(lesson2) + 1, exercise2)

def add_exercise(schedule, lesson):
    exercise = f"{lesson}-Exercise"
    if lesson in schedule:
        if exercise not in schedule:
            idx = schedule.index(lesson)
            schedule.insert(idx + 1, exercise)
    else:
        schedule.append(lesson)
        schedule.append(exercise)

def print_schedule(schedule):
    for i, lesson in enumerate(schedule, 1):
        print(f"{i}.{lesson}")


schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]
    lesson = parts[1]

    if action == "Add":
        add_lesson(schedule, lesson)
    elif action == "Insert":
        index = int(parts[2])
        insert_lesson(schedule, lesson, index)
    elif action == "Remove":
        remove_lesson(schedule, lesson)
    elif action == "Swap":
        lesson2 = parts[2]
        swap_lessons(schedule, lesson, lesson2)
    elif action == "Exercise":
        add_exercise(schedule, lesson)

print_schedule(schedule)