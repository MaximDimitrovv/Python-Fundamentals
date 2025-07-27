n = int(input())
plant_info = {}

for _ in range(n):
    info = input().split("<->")
    plant_info[info[0]] = {"Rarity": info[1], "Rating": []}

while (command := input()) != "Exhibition":
    split_command = command.split(": ")
    plant_info_split = split_command[1].split(" - ")

    match split_command[0]:
        case "Rate":
            plant_name = plant_info_split[0]
            rate = int(plant_info_split[1])
            if plant_name not in plant_info:
                print("error")
            else:
                plant_info[plant_name]["Rating"].append(rate)
        case "Update":
            plant_name = plant_info_split[0]
            new_rarity = plant_info_split[1]
            if plant_name not in plant_info:
                print('error')
            else:
                plant_info[plant_name]["Rarity"] = new_rarity
        case "Reset":
            plant_name = plant_info_split[0]
            if plant_name not in plant_info:
                print('error')
            else:
                plant_info[plant_name]["Rating"] = []
print("Plants for the exhibition:")
for info in plant_info.items():
    plant_name = info[0]
    rating_list = info[1]["Rating"]
    rarity = info[1]["Rarity"]
    average_rating = 0
    if rating_list:
        average_rating = sum(rating_list) / len(rating_list)
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")

