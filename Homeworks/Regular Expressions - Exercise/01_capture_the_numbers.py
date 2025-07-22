import re

all_matches = []
data = input()

while data:
    pattern = r'\d+'
    matches = re.findall(pattern, data)
    if matches:
        all_matches += matches
    data = input()

print(" ".join(all_matches))