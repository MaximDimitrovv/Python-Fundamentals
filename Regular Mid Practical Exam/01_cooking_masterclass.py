from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

free_pack_flour = 0

for student in range(1, students + 1):
    if student % 5 == 0:
        free_pack_flour += 1

percent = students * 0.2
total_apron_price = apron_price * (students + ceil(percent))
total_egg_price = (egg_price * 10) * students
total_flour_price = flour_price * (students - free_pack_flour)

total = total_flour_price + total_apron_price + total_egg_price

if budget >= total:
    print(f"Items purchased for {total:.2f}$.")
else:
    money_needed = total - budget
    print(f"{money_needed:.2f}$ more needed.")


