numbers_of_orders = int(input())
total = 0

for order in range(1, numbers_of_orders + 1):

    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())


    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        order_price = price_per_capsule * days * capsules_needed_per_day
        total += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")