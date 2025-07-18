foods = {}
sold = 0

while "Complete" not in (line := input().split()):

    command = line[0]
    quantity = int(line[1])
    food = line[2]


    if command == "Receive":
        if quantity <= 0:
            continue

        if food not in foods:
            foods[food] = quantity
        else:
            foods[food] += quantity

    elif command == "Sell":
        if food not in foods:
            print(f"You do not have any {food}.")
            continue

        if quantity > foods[food]:
            print(f"There aren't enough {food}. You sold the last {foods[food]} of them.")
            sold += foods[food]
            foods.pop(food)
            continue
        else:
            print(f"You sold {quantity} {food}.")
            foods[food] -= quantity
            if foods[food] == 0:
                foods.pop(food)

        sold += quantity

for food, quantity in foods.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold} goods")