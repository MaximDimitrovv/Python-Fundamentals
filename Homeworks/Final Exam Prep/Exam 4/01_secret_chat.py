message = input()

while (command := input()) != "Reveal":
    command_split = command.split(":|:")
    action = command_split[0]

    match action:
        case "InsertSpace":
            index = int(command_split[1])
            message = message[:index] + " " + message[index:]
            print(message)
        case "Reverse":
            substring = command_split[1]
            start_index = message.find(substring)

            if start_index != -1:
                end_index = (start_index + len(substring))
                message = message[:start_index] + "" + message[end_index:]
                message += substring[::-1]
                print(message)
            else:
                print("error")

        case "ChangeAll":
            substring = command_split[1]
            replacement = command_split[2]

            message = message.replace(substring, replacement)
            print(message)

print(f'You have a new text message: {message}')