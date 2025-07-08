countries = input().split(", ")
capitals = input().split(", ")

doubles = tuple(zip(countries, capitals))

for country, city in doubles:
    print(f"{country} -> {city}")