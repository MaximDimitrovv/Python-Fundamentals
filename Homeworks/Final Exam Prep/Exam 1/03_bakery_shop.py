foods = {}

while "Complete" not in (line := input().split()):

    if "Receive" in line:
        quantity = line[1]
        food = line[2]
        if food not in foods:
            foods[food] = quantity
        else:
            foods[food] += quantity
