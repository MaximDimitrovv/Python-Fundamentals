import re

date = input()

pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

matches = re.findall(pattern, date)

for char in matches:
    day = char[0]
    sep = char[1]
    month = char[2]
    year = char[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
