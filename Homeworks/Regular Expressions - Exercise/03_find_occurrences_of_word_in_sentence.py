import re

string = input()
word = input()

pattern = fr'\b{word.lower()}\b'
matches = re.findall(pattern, string.lower())

print(len(matches))