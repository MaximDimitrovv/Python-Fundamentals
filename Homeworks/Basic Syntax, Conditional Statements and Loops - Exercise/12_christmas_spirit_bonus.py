quantity_of_decorations = int(input())
days = int(input())

christmas_spirit_points = 0
total_price = 0

for day in range(1, days + 1):

    tree_light_price = 0
    tree_garland_price = 0
    tree_skirt_price = 0
    ornament_price = 0

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        ornament_price = quantity_of_decorations * 2
        christmas_spirit_points += 5

    if day % 3 == 0:
        tree_skirt_price = quantity_of_decorations * 5
        tree_garland_price = quantity_of_decorations * 3
        christmas_spirit_points += 13

    if day % 5 == 0:
        if day % 3 == 0:
            christmas_spirit_points += 30
        tree_light_price = quantity_of_decorations * 15
        christmas_spirit_points += 17

    total_price += tree_light_price + tree_garland_price + tree_skirt_price + ornament_price

    if day % 10 == 0:

        tree_skirt_price = 5
        tree_garland_price = 3
        tree_light_price = 15
        christmas_spirit_points -= 20

        total_price += tree_light_price + tree_garland_price + tree_skirt_price

if days % 10 == 0:
    christmas_spirit_points -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit_points}")
