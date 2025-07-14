people_to_elevate = int(input())
capacity = int(input())
courses = 0

while people_to_elevate > 0:
    courses += 1
    people_to_elevate -= capacity

print(courses)