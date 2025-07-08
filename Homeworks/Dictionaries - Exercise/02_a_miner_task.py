
resources = {}

while (line := input()) != "stop":
    resource = line
    quantity = int(input())

    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for key, value in resources.items():
    print(f"{key} -> {value}")