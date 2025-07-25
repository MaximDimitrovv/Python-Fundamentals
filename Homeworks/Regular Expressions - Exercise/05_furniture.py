import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)\b'
furniture_list = []
total_price = 0


while (line := input()) != "Purchase":
    match = re.search(pattern, line)
    if match:
        furniture, price, quantity = match.groups()
        furniture_list.append(furniture)
        total_price += float(price) * int(quantity)

print("Bought furniture:")
for name in furniture_list:
    print(name)
print(f"Total money spend: {total_price:.2f}")
