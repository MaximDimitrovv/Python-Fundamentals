numbers = list(map(int, input().split(", ")))

group = 10
while numbers:
    group_nums = [n for n in numbers if group - 9 <= n <= group]
    print(f"Group of {group}'s: {group_nums}")
    numbers = [n for n in numbers if n not in group_nums]
    group += 10


