
city_info = {}

while (info := input()) != "Sail":
    split_info = info.split("||")
    name = split_info[0]
    population = int(split_info[1])
    gold = int(split_info[2])
    if name in city_info:
        city_info[name]["Population"] += population
        city_info[name]["Gold"] += gold
    else:
        city_info[name] = {"Population": population, "Gold": gold}

while (command := input()) != "End":
    split_command = command.split("=>")
    action = split_command[0]
    town = split_command[1]

    match action:
        case "Plunder":
            people = int(split_command[2])
            gold = int(split_command[3])

            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            city_info[town]["Population"] -= people
            city_info[town]["Gold"] -= gold

            if city_info[town]["Population"] < 1 or city_info[town]["Gold"] < 1:
                print(f"{town} has been wiped off the map!")
                city_info.pop(town)

        case "Prosper":
            gold = int(split_command[2])

            if gold < 0:
                print("Gold added cannot be a negative number!")
            else:
                city_info[town]["Gold"] += gold
                total_gold = city_info[town]["Gold"]
                print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")

if len(city_info) > 0:
    print(f"Ahoy, Captain! There are {len(city_info)} wealthy settlements to go to:")

    for name, info in city_info.items():
        population = info["Population"]
        gold = info["Gold"]
        print(f"{name} -> Population: {population} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
