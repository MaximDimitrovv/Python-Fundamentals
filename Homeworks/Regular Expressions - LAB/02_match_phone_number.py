import re

phone_number = input()

pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

match = re.findall(pattern, phone_number)

print(", ".join(match))