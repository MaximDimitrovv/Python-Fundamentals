
string = input()

while (command := input()) != "Done":
    split_command = command.split(" ")
    action = split_command[0]

    match action:
        case "TakeOdd":
            new_string = ''
            for i in range(len(string)):
                if i % 2 != 0:
                    new_string += string[i]
            string = new_string
            print(string)
        case "Cut":
            start_index = int(split_command[1])
            length = int(split_command[2])
            end_index = start_index + length

            string = string[:start_index] + string[end_index:]
            print(string)
        case "Substitute":
            substring = split_command[1]
            substitute = split_command[2]

            if substring in string:
                string = string.replace(substring, substitute)
                print(string)
            else:
                print("Nothing to replace!")

print(f"Your password is: {string}")