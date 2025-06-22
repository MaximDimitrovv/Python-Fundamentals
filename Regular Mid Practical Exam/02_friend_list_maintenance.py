friends = input().split(", ")
blacklisted = 0
lost_names = 0

while True:
    command = input()

    if command == "Report":
        print(f"Blacklisted names: {blacklisted}")
        print(f"Lost names: {lost_names}")
        print(" ".join(friends))
        break

    if "Blacklist" in command:
        split_command = command.split(" ")
        name = split_command[1]

        if name not in friends:
            print(f"{name} was not found.")
        else:
            for i in range(len(friends)):
                if friends[i] == name:
                    friends[i] = "Blacklisted"
            blacklisted += 1
            print(f"{name} was blacklisted.")

    if "Error" in command:
        split_command = command.split(" ")
        index = int(split_command[1])

        if 0 <= index < len(friends):
            if friends[index] != "Blacklisted" and friends[index] != "Lost":
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = "Lost"
                lost_names += 1

    if "Change" in command:
        split_command = command.split(" ")
        index = int(split_command[1])
        new_name = split_command[2]

        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name