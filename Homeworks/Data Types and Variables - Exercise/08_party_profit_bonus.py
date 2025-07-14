group_size = int(input())
days_adventuring = int(input())
coins = 0

for day in range(1, days_adventuring + 1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins += 50
    coins  -= group_size * 2


    if day % 5 == 0:
        coins += group_size * 20

    if day % 3 == 0:
        if day % 5 == 0:
            coins -= group_size * 2
        coins -= group_size * 3

split_coins = int(coins / group_size)
print(f"{group_size} companions received {split_coins} coins each.")
