import re
from re import search

list_names = input().split(", ")
statistic = {}

while (line := input()) != "end of race":
    name = ''
    points = 0

    pattern = r'[a-zA-Z]'
    pattern_digits = r'\d'

    match_name = re.findall(pattern, line)

    if match_name:
        for letter in match_name:
            name += letter

        if name in list_names:
            match_digits = re.findall(pattern_digits, line)

            for digit in match_digits:
                points += int(digit)
            if name not in statistic:
                statistic[name] = points
            else:
                statistic[name] += points

if statistic:
    sorted_dict = dict(sorted(statistic.items(), key=lambda x: x[1], reverse=True))
    i = 1
    for name, points in sorted_dict.items():
        if i == 1:
            print(f"{i}st place: {name}")
        elif i == 2:
            print(f"{i}nd place: {name}")
        elif i == 3:
            print(f"{i}rd place: {name}")
            break
        i += 1

