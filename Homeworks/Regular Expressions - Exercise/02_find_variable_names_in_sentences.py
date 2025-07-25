import re

data = input()

pattern = r'\b[_][A-Za-z0-9]+\b'
matches = re.findall(pattern, data)
matches_list = []

for match in matches:
    string = ''
    for letter in match:
        if not letter == "_":
            string += letter
    matches_list.append(string)

print(",".join(matches_list))