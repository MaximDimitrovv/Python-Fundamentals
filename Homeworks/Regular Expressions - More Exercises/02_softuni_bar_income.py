import re


pattern = r"%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?(\d+(?:\.\d+)?)\$"

customer_info = {}
total_income = 0

while (data := input()) != "end of shift":
    match = re.search(pattern, data)
    if match:
        name = match.group(1)
        product = match.group(2)
        quantity = int(match.group(3))
        price = float(match.group(4))
        total = quantity * price
        print(f"{name}: {product} - {total:.2f}")
        total_income += total

print(f'Total income: {total_income:.2f}')
