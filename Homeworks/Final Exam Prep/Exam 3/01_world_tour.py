stops_string = input()

while (command := input()) != "Travel":
    split_command = command.split(":")

    action = split_command[0]

    match action:
        case "Add Stop":
            index = int(split_command[1])
            string = split_command[2]
            if 0 <= index < len(stops_string):
                stops_string = stops_string[:index] + string + stops_string[index:]
                print(stops_string)
            else:
                print(stops_string)
        case "Remove Stop":
            start_index = int(split_command[1])
            end_index = int(split_command[2])
            if 0 <= start_index < len(stops_string) and 0 <= end_index < len(stops_string):
                stops_string = stops_string.replace(stops_string[start_index:end_index + 1], "")
                print(stops_string)
            else:
                print(stops_string)
        case "Switch":
            old_string = split_command[1]
            new_string = split_command[2]
            if old_string in stops_string:
                stops_string = stops_string.replace(old_string, new_string)
                print(stops_string)
            else:
                print(stops_string)
print(f"Ready for world tour! Planned stops: {stops_string}")

