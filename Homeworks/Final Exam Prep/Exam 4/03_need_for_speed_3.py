n = int(input())

car_info_dict = {}

for _ in range(n):
    car_info = input().split("|")

    model = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])

    car_info_dict[model] = {"Mileage": mileage, "Fuel": fuel}

while (command := input()) != "Stop":
    command_split = command.split(" : ")
    action = command_split[0]

    match action:
        case "Drive":
            model = command_split[1]
            distance = int(command_split[2])
            fuel = int(command_split[3])

            if fuel <= car_info_dict[model]["Fuel"]:
                car_info_dict[model]["Mileage"] += distance
                car_info_dict[model]["Fuel"] -= fuel
                print(f"{model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if car_info_dict[model]["Mileage"] >= 100000:
                    print(f"Time to sell the {model}!")
                    car_info_dict.pop(model)
            else:
                print("Not enough fuel to make that ride")
        case "Refuel":
            model = command_split[1]
            fuel = int(command_split[2])

            if (car_info_dict[model]["Fuel"] + fuel) > 75:
                fuel_needed = 75 - car_info_dict[model]["Fuel"]
                car_info_dict[model]["Fuel"] = 75
                print(f"{model} refueled with {fuel_needed} liters")
            else:
                print(f"{model} refueled with {fuel} liters")
                car_info_dict[model]["Fuel"] += fuel
        case "Revert":
            model = command_split[1]
            kilometers = int(command_split[2])

            car_info_dict[model]["Mileage"] -= kilometers
            if car_info_dict[model]["Mileage"] < 10000:
                car_info_dict[model]["Mileage"] = 10000
            else:
                print(f"{model} mileage decreased by {kilometers} kilometers")

for model, info in car_info_dict.items():
    mileage = info["Mileage"]
    fuel = info["Fuel"]
    print(f"{model} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")