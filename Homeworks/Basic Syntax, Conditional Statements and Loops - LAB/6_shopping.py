budget = int(input())

total_price = 0

while budget >= total_price:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    price = int(command)
    total_price += price

else:
    print("You went in overdraft!")