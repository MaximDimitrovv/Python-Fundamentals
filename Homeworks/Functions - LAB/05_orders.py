def total_price(type_product, product_quantity):
    if type_product == "coffee":
        return 1.50 * product_quantity
    elif type_product == "water":
        return 1 * product_quantity
    elif type_product == "coke":
        return 1.40 * product_quantity
    elif type_product == "snacks":
        return 2 * product_quantity


product = input()
quantity = int(input())

print(f"{total_price(product, quantity):.2f}")
