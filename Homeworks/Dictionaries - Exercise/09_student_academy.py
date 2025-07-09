n = int(input())

stat = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in stat:
        stat[name] = []

    stat[name].append(grade)

for name, grade in stat.items():
    if (sum(grade) / len(grade)) >= 4.5:
        print(f"{name} -> {sum(grade) / len(grade):.2f}")