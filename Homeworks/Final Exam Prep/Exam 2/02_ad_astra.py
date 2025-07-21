import re

data = input()

pattern = r'([#|])(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1'

matches = re.finditer(pattern, data)

info = []
total_calories = 0

for match in matches:
    item = match.group("item")
    date = match.group("date")
    calories = int(match.group("calories"))

    info.append([item, date, calories])
    total_calories += calories

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for item_data in info:
    print(f"Item: {item_data[0]}, Best before: {item_data[1]}, Nutrition: {item_data[2]}")