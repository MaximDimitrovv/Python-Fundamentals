fires_with_cells = input()
water = int(input())

diff_fires = fires_with_cells.split("#")
data_in_range = []
valid_cells = []

for data in diff_fires:
    parts = data.split(" = ")

    type_of_fire = parts[0]
    range_of_fire = int(parts[1])

    if type_of_fire == "High" and 81 <= range_of_fire <= 125:
        data_in_range.append(parts)
    elif type_of_fire == "Medium" and 51 <= range_of_fire <= 80:
        data_in_range.append(parts)
    elif type_of_fire == "Low" and 1 <= range_of_fire <= 50:
        data_in_range.append(parts)
    else:
        continue

effort = 0
total_fire = 0


for data in data_in_range:
    cells = int(data[1])
    if water >= cells:
        water -= cells
        effort += cells * 0.25
        total_fire += cells
        valid_cells.append(cells)

print("Cells:")
for print_data in valid_cells:
    print(f"- {print_data}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
