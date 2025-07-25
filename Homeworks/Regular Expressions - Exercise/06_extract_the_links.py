import re

string = input()
pattern = r'(w{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+)'

while string:
    match = re.search(pattern, string)
    if match:
        print(match.group(1))

    string = input()

