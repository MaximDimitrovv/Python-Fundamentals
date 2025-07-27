import re

string = input()
pattern = r'=([A-Z][a-zA-Z]{2,})=|/([A-Z][a-zA-Z]{2,})/'
points = 0

matches = re.findall(pattern, string)
result = [match[0] if match[0] else match[1] for match in matches]

for destination in result:
    points += len(destination)

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {points}")
