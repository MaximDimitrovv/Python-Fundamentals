items = input()
budget = float(input())
selling_money = 0

separated_items = items.split("|")
prices = []

for items in separated_items:
    prices.append(items.split("->"))


new_prices = []
profit = 0
money_from_sales = 0

for item_price in prices:
    type_of_item = item_price[0]
    price_of_item = float(item_price[1])

    if type_of_item == "Clothes" and price_of_item <= 50 and budget >= price_of_item:
        selling_price = price_of_item + (price_of_item * 0.4)
        new_prices.append(selling_price)
        budget -= price_of_item
        selling_money += selling_price
        profit += selling_price - price_of_item
        money_from_sales += selling_price

    elif type_of_item == "Shoes" and price_of_item <= 35 and budget >= price_of_item:
        selling_price = price_of_item + (price_of_item * 0.4)
        new_prices.append(selling_price)
        budget -= price_of_item
        selling_money += selling_price
        profit += selling_price - price_of_item
        money_from_sales += selling_price

    elif type_of_item == "Accessories" and price_of_item <= 20.5 and budget >= price_of_item:
        selling_price = price_of_item + (price_of_item * 0.4)
        new_prices.append(selling_price)
        budget -= price_of_item
        selling_money += selling_price
        profit += selling_price - price_of_item
        money_from_sales += selling_price


for price in new_prices:
    print(f"{price:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

total_money = budget + money_from_sales

if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")