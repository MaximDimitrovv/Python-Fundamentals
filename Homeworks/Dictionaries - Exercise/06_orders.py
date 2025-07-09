
def calculate_prices(dictionary):
    result = []
    for key, value in dictionary.items():
        total_price = 1
        for k, v in value.items():
            total_price *= v
        result.append(f"{key} -> {total_price:.2f}")
    return "\n".join(result)


products = {}

while "buy" not in (line := input().split(' ')):

    name = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if name not in products:
        products[name] = {"price": price,"quantity": quantity}
    else:

        products[name]["price"] = price
        products[name]["quantity"] += quantity

print(calculate_prices(products))

