import re
n = int(input())

pattern = r'^[|]([A-Z]{4,})[|]:#([A-za-z]+\s[A-Za-z]+)#'


for i in range(n):
    string = input()

    matches = re.findall(pattern, string)

    if matches:
        for name, title in matches:
            print(f"{name}, The {title}\n>> Strength: {len(name)}\n>> Armor: {len(title)}"
)
    else:
        print("Access denied!")