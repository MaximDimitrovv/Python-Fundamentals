element = input().split(" ")

bakery = {}

for i in range(0, len(element), 2):
    food = element[i]
    quantity = element[i + 1]

    bakery[food] = int(quantity)

print(bakery)
