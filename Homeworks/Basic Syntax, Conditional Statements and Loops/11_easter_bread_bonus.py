budget = float(input())
flour_price_kg = float(input())

eggs_price_pack = flour_price_kg * (75 / 100)
milk_price_liter = flour_price_kg + (flour_price_kg * (25 / 100))
milk_for_one_loaves = milk_price_liter / 4
one_loaves_price = flour_price_kg + eggs_price_pack + milk_for_one_loaves


current_bread_count = 0
colored_eggs = 0
money_left = 0


while budget > one_loaves_price:
    current_bread_count += 1
    colored_eggs += 3
    for eggs in range(current_bread_count, 0, -1):
        if eggs % 3 == 0:
            colored_eggs = colored_eggs - (current_bread_count - 2)
        else:
            break
    budget -= one_loaves_price
    money_left = budget

if money_left == 0:
    money_left = budget

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")



