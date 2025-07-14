lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shield_counter = 0
total_price = 0

for lose in range(1, lost_fights + 1):

    if lose % 2 == 0:
        total_price += helmet_price

    if lose % 3 == 0:
        if lose % 2 == 0:
            total_price += shield_price
            broken_shield_counter += 1
        total_price += sword_price

    if broken_shield_counter == 2:
        total_price += armor_price
        broken_shield_counter = 0

print(f"Gladiator expenses: {total_price:.2f} aureus")