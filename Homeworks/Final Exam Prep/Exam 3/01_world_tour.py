import re

n = int(input())
plant_dict = {}

for _ in range(n):
    plant_info = input().split("<->")
    plant_dict[plant_info[0]] = {"Rarity":int(plant_info[1])}

print(plant_dict)
pattern = r'\b([a-zA-Z]+):\s([a-zA-Z]+)\s-\s([\d]+)'

while (string := input()) != "Exhibition":
    match = re.search(pattern, string)
    if match:
        command = match.group(1)
        if command == "Rate":
            pass
        elif command == "Update":
            pass
        elif command == "Reset":
            pass
