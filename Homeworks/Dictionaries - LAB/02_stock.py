components = input().split(" ")

products = {}

for i in range(0, len(components), 2):
    food = components[i]
    quantity = components[i + 1]
    products[food] = quantity

food_search = input().split(" ")

for item in food_search:
    if item not in products:
        print(f"Sorry, we don't have {item}")
    else:
        print(f"We have {products[item]} of {item} left")

