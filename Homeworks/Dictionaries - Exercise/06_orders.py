products = {
    'products':
        {

        }
}

while "buy" not in (line := input().split(' ')):

    name = line[0]
    price = float(line[1])
    quantity = int(line[2])

    if name not in products["products"]:
        products["products"][name] = quantity

    # else:
    #     products['price'] = price
    #     products['quantity'] = quantity

    print(products)