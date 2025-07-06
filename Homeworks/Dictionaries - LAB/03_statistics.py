products = {}

while (line := input()) != 'statistics':
    product, quantity = line.split(": ")

    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)

print("Products in stock:")

for item, quantity in products.items():
    print(f"- {item}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")