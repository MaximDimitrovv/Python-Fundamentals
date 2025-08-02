string = input()

while (command := input()) != "Generate":
    split_command = command.split(">>>")
    action = split_command[0]

    match action:
        case "Contains":
            substring = split_command[1]
            if substring in string:
                print(f"{string} contains {substring}")
            else:
                print("Substring not found!")
        case "Flip":
            start_index = int(split_command[2])
            end_index = int(split_command[3])
            if split_command[1] == "Upper":
                new_string = string[start_index:end_index].upper()
                string = string[:start_index] + new_string + string[end_index:]
            elif split_command[1] == "Lower":
                new_string = string[start_index:end_index].lower()
                string = string[:start_index] + new_string + string[end_index:]
            print(string)

        case "Slice":
            start_index = int(split_command[1])
            end_index = int(split_command[2])

            string = string[:start_index] + string[end_index:]
            print(string)
print(f"Your activation key is: {string}")