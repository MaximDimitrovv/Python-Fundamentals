import re
from re import finditer

data = input()

valid_names = []
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

matches = re.findall(pattern, data)

for name in matches:
    print(name, end=" ")
