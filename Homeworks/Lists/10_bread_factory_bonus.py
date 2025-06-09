commands = input()

energy = 100
coins = 100

list_of_commands = commands.split("|")
split_commands = []

for command in list_of_commands:
    split_commands.append(command.split("-"))


for split_list in split_commands:
    type_command = split_list[0]
    number_command = int(split_list[1])

    if type_command == "rest":
        is_energy_above = energy + number_command

        if is_energy_above <= 100:
            energy += number_command
            print(f"You gained {number_command} energy.")
        else:
            needed_energy = 100 - energy
            energy += needed_energy
            print(f"You gained {needed_energy} energy.")

        print(f"Current energy: {energy}.")

    elif type_command == "order":
        is_enough_energy = energy - 30

        if is_enough_energy >= 0:
            energy -= 30
            coins += number_command
            print(f"You earned {number_command} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number_command:
            coins -= number_command
            print(f"You bought {type_command}.")
        else:
            print(f"Closed! Cannot afford {type_command}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

